# filename: openai_documents_access_v1.py
import openai

# Set your OpenAI API key here
openai.api_key = 'YOUR_OPENAI_API_KEY'

def list_documents():
    # List the documents in your OpenAI account storage
    response = openai.File.list()
    return response['data']

def retrieve_document(file_id):
    # Retrieve a specific document using its unique file ID
    response = openai.File.download(file_id)
    return response.content.decode('utf-8')  # Assuming the file is text

# Example usage:
if __name__ == '__main__':
    # List documents and print the metadata
    document_metadata = list_documents()
    print(document_metadata)

    # Use a specific file_id from the listed documents to download it
    # (Uncomment the lines below and replace 'YOUR_FILE_ID' with your actual file ID)
    # file_id = 'YOUR_FILE_ID'
    # document_content = retrieve_document(file_id)
    # print(document_content)