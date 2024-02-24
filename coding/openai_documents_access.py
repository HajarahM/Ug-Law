# filename: openai_documents_access.py
import openai

# Set your OpenAI API key here
openai.api_key = 'YOUR_OPENAI_API_KEY'

def list_documents():
    # List the documents in your OpenAI account storage
    response = openai.File.list()
    return response

def retrieve_document(file_id):
    # Retrieve a specific document using its unique file ID
    response = openai.File.download(file_id)
    # Response contents are binary, decode if necessary. e.g., response.content.decode('utf-8') for text files
    return response.content

# Example usage:
if __name__ == '__main__':
    # List documents and print them
    documents = list_documents()
    print(documents)

    # Uncomment the following lines to retrieve a specific file by file_id and print the content
    # Make sure to replace YOUR_FILE_ID with the actual value.
    # file_id = 'YOUR_FILE_ID'
    # content = retrieve_document(file_id)
    # print(content)