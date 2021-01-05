// Create an ExecutionContext using 
// credentials and create a new 
// operation instance.
const executionContext = PDFToolsSdk.ExecutionContext.create(credentials),
exportPDF = PDFToolsSdk.ExportPDF,
exportPdfOperation = exportPDF.Operation.createNew(exportPDF.SupportedTargetFormats.DOCX);

// Set operation input from a source file
const input = PDFToolsSdk.FileRef.createFromLocalFile('resources/exportPDFInput.pdf');
exportPdfOperation.setInput(input);

// Execute the operation and Save the result to the specified location.
exportPdfOperation.execute(executionContext)
.then(result => result.saveAsFile('output/exportPdfOutput.docx'))
