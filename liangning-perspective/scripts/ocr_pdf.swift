import AppKit
import Foundation
import PDFKit
import Vision

func usage() -> Never {
    fputs("usage: ocr_pdf.swift INPUT.pdf OUTPUT.txt [startPage] [endPage]\n", stderr)
    exit(2)
}

guard CommandLine.arguments.count >= 3 else { usage() }

let input = URL(fileURLWithPath: CommandLine.arguments[1])
let output = URL(fileURLWithPath: CommandLine.arguments[2])
let startPage = CommandLine.arguments.count >= 4 ? max(1, Int(CommandLine.arguments[3]) ?? 1) : 1
let requestedEndPage = CommandLine.arguments.count >= 5 ? Int(CommandLine.arguments[4]) : nil

guard let document = PDFDocument(url: input) else {
    fputs("failed to open PDF: \(input.path)\n", stderr)
    exit(1)
}

let pageCount = document.pageCount
let endPage = min(requestedEndPage ?? pageCount, pageCount)
guard startPage <= endPage else {
    fputs("invalid page range\n", stderr)
    exit(2)
}

func cgImage(for page: PDFPage, scale: CGFloat = 2.0) -> CGImage? {
    let bounds = page.bounds(for: .mediaBox)
    let size = NSSize(width: bounds.width * scale, height: bounds.height * scale)
    let image = page.thumbnail(of: size, for: .mediaBox)
    var proposed = CGRect(origin: .zero, size: image.size)
    return image.cgImage(forProposedRect: &proposed, context: nil, hints: nil)
}

func recognize(_ image: CGImage) throws -> String {
    let request = VNRecognizeTextRequest()
    request.recognitionLevel = .accurate
    request.usesLanguageCorrection = true

    let handler = VNImageRequestHandler(cgImage: image, options: [:])
    try handler.perform([request])

    let observations = request.results ?? []
    return observations.compactMap { observation in
        observation.topCandidates(1).first?.string
    }.joined(separator: "\n")
}

var chunks: [String] = []
for pageNumber in startPage...endPage {
    autoreleasepool {
        guard let page = document.page(at: pageNumber - 1), let image = cgImage(for: page) else {
            chunks.append("\n\n# PAGE \(pageNumber)\n\n[OCR failed: render error]")
            return
        }

        do {
            let text = try recognize(image).trimmingCharacters(in: .whitespacesAndNewlines)
            chunks.append("\n\n# PAGE \(pageNumber)\n\n\(text)")
            print("ocr page \(pageNumber)/\(endPage)")
            fflush(stdout)
        } catch {
            chunks.append("\n\n# PAGE \(pageNumber)\n\n[OCR failed: \(error)]")
            print("ocr page \(pageNumber)/\(endPage) failed: \(error)")
            fflush(stdout)
        }
    }
}

let result = chunks.joined(separator: "\n")
try result.write(to: output, atomically: true, encoding: .utf8)
