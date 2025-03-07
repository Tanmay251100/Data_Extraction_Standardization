import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dotenv import load_dotenv
from utils.azure.document_intelligence import extracter
from utils.aws.s3 import get_s3_client, read_pdf_from_s3
from utils.azure.document_intelligence import get_doc_int_client

load_dotenv()


url = 'https://sfopenaccessbucket.s3.us-east-1.amazonaws.com/uploads/649af4f1-a280-43b3-8135-1664e7db178b.pdf'

print(extracter(get_doc_int_client(), get_s3_client(), url))