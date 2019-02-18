# export GOOGLE_APPLICATION_CREDENTIALS = "creds.json"
import os
import io

credential_path = "creds.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


def detect_document(path):
    output = ""
    """Detects document features in an image."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.document_text_detection(image=image)

    # print(response.full_text_annotation.pages.page.blocks)

    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            # print('\nBlock confidence: {}\n'.format(block.confidence))
            for paragraph in block.paragraphs:
                # print('Paragraph confidence: {}'.format(paragraph.confidence))
                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    # print('Word text: {} (confidence: {})'.format(word_text, word.confidence))
                    for symbol in word.symbols:
                        # print('\tSymbol: {} (confidence: {})'.format(ymbol.text, symbol.confidence))
                        output += symbol.text
    
    # print(output)
    return output


if __name__ == "__main__":
    print("why call this? call cli.py")