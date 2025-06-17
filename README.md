🧠 Flashcard Generation Tool

This is a lightweight and efficient tool that uses Large Language Models (LLMs) like OpenAI’s GPT to convert educational content into effective flashcards (Question-Answer format). It's perfect for students, educators, or anyone looking to study or revise material quickly.

—

📌 Features

    📄 Input: Accepts raw text or PDF content

    ✨ Preprocessing: Cleans and optimizes input text

    🤖 LLM-Powered: Uses GPT (or other LLMs) to generate flashcards

    🧾 Output Format: Structured flashcards (Q/A pairs) in JSON or CSV

    🖥️ Interface: Streamlit-based user interface for ease of use

    💾 Export: Save flashcards for offline use or review

—

📂 Project Structure

flashcard_tool/
├── main.py # Core script to drive functionality
├── streamlit_app.py # Streamlit front-end
├── utils/
│ ├── preprocess.py # Input cleaning and formatting
│ ├── parse_output.py # Convert LLM output into Q/A format
│ └── save_flashcards.py # JSON/CSV export functionality
├── flashcards/
│ └── output.json # Sample or generated flashcards
├── .env # OpenAI API Key (not pushed to GitHub)
├── requirements.txt # Project dependencies
└── README.md # You’re reading it!

—

⚙️ Installation & Setup

    Clone the repository:

git clone https://github.com/your-username/flashcard-tool.git
cd flashcard-tool

    Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

    Install dependencies:

pip install -r requirements.txt

    Set your OpenAI API key in a .env file:

.env

OPENAI_API_KEY=your_openai_key_here

    Run the Streamlit app:

streamlit run streamlit_app.py

—

🧪 Usage

You can use the tool in two ways:

    CLI (main.py):

    Paste or load text/PDF

    Output flashcards printed and saved

    Web UI (streamlit_app.py):

    Upload a PDF or paste content

    Click "Generate"

    Edit/review Q&A

    Download flashcards as JSON/CSV

—

📦 Output Format

Example flashcard in JSON:

[
{
"question": "What is the function of the mitochondria?",
"answer": "It produces energy for the cell through cellular respiration."
},
...
]

—

🛠️ Dependencies

    Python 3.8+

    openai

    streamlit

    python-dotenv

    PyPDF2

    pandas

Install via:

pip install -r requirements.txt

—

📚 Prompt Template (used internally)

Generate 5 flashcards (Question and Answer format) from the following content:
[educational content here]

Format:
Q1: [question]
A1: [answer]
...

libraries used
absl-py==2.1.0
agent==0.1.3
aiohappyeyeballs==2.6.1
aiohttp==3.11.18
aiosignal==1.3.2
alembic==1.16.1
altair==5.5.0
annotated-types==0.7.0
anyio==4.9.0
argon2-cffi==23.1.0
argon2-cffi-bindings==21.2.0
arrow==1.3.0
asttokens==2.4.1
astunparse==1.6.3
async-lru==2.0.5
attrs==24.2.0
Authlib==1.5.2
babel==2.17.0
banal==1.0.6
beautifulsoup4==4.13.4
bleach==6.2.0
blinker==1.9.0
cachetools==5.5.2
certifi==2024.8.30
cffi==1.17.1
charset-normalizer==3.4.0
click==8.1.8
colorama==0.4.6
comm==0.2.2
contextlib2==21.6.0
contourpy==1.3.0
cryptography==44.0.3
cycler==0.12.1
Cython==3.1.1
dataset==1.6.2
dataset-utils==0.0.48
debugpy==1.8.7
decoder==0.5
decorator==5.1.1
defusedxml==0.7.1
Deprecated==1.2.18
distro==1.9.0
docstring_parser==0.16
executing==2.1.0
fastapi==0.115.12
fastjsonschema==2.21.1
filelock==3.18.0
flatbuffers==24.3.25
fonttools==4.54.1
fqdn==1.5.1
frozendict==2.4.6
frozenlist==1.6.0
fsspec==2025.3.2
gast==0.6.0
gitdb==4.0.12
GitPython==3.1.44
google-adk==0.3.0
google-ai-generativelanguage==0.6.15
google-api-core==2.25.0rc0
google-api-python-client==2.169.0
google-auth==2.39.0
google-auth-httplib2==0.2.0
google-cloud-aiplatform==1.91.0
google-cloud-bigquery==3.31.0
google-cloud-core==2.4.3
google-cloud-resource-manager==1.14.2
google-cloud-secret-manager==2.23.3
google-cloud-speech==2.32.0
google-cloud-storage==2.19.0
google-cloud-trace==1.16.1
google-crc32c==1.7.1
google-genai==1.13.0
google-generativeai==0.8.5
google-pasta==0.2.0
google-resumable-media==2.7.2
googleapis-common-protos==1.70.0
graphviz==0.20.3
greenlet==3.2.1
grpc-google-iam-v1==0.14.2
grpcio==1.71.0
grpcio-status==1.71.0
h11==0.16.0
h5py==3.12.1
httpcore==1.0.9
httplib2==0.22.0
httpx==0.28.1
httpx-sse==0.4.0
huggingface-hub==0.30.2
idna==3.10
importlib_metadata==8.6.1
ipykernel==6.29.5
ipython==8.29.0
ipywidgets==8.1.7
isoduration==20.11.0
jax==0.4.35
jaxlib==0.4.35
jedi==0.19.1
Jinja2==3.1.6
jiter==0.9.0
joblib==1.4.2
json5==0.12.0
jsonpointer==3.0.0
jsonschema==4.23.0
jsonschema-specifications==2025.4.1
jupyter==1.1.1
jupyter-console==6.6.3
jupyter-events==0.12.0
jupyter-lsp==2.2.5
jupyter_client==8.6.3
jupyter_core==5.7.2
jupyter_server==2.16.0
jupyter_server_terminals==0.5.3
jupyterlab==4.4.3
jupyterlab_pygments==0.3.0
jupyterlab_server==2.27.3
jupyterlab_widgets==3.0.15
kaggle==1.6.17
kagglehub==0.3.3
keras==3.7.0
keras-utils==1.0.13
kiwisolver==1.4.7
libclang==18.1.1
litellm==1.66.3
lxml==5.4.0
Mako==1.3.10
Markdown==3.7
markdown-it-py==3.0.0
MarkupSafe==3.0.2
matplotlib==3.9.2
matplotlib-inline==0.1.7
mcp==1.7.1
mdurl==0.1.2
mediapipe==0.10.14
mistune==3.1.3
ml_dtypes==0.5.1
multidict==6.4.3
multitasking==0.0.11
namex==0.0.8
narwhals==1.42.1
nbclient==0.10.2
nbconvert==7.16.6
nbformat==5.10.4
nest-asyncio==1.6.0
notebook==7.4.3
notebook_shim==0.2.4
numpy==2.0.2
openai==0.28.0
opencv-contrib-python==4.10.0.84
opencv-python==4.10.0.84
opencv-python-headless==4.10.0.84
opentelemetry-api==1.32.1
opentelemetry-exporter-gcp-trace==1.9.0
opentelemetry-resourcedetector-gcp==1.9.0a0
opentelemetry-sdk==1.32.1
opentelemetry-semantic-conventions==0.53b1
opt_einsum==3.4.0
optree==0.13.0
overrides==7.7.0
packaging==24.2
pandas==2.2.3
pandocfilters==1.5.1
parso==0.8.4
peewee==3.18.1
pillow==11.0.0
platformdirs==4.3.6
prometheus_client==0.22.0
prompt_toolkit==3.0.48
propcache==0.3.1
proto-plus==1.26.1
protobuf==5.29.4
psutil==5.9.5
pure_eval==0.2.3
pyarrow==20.0.0
pyasn1==0.6.1
pyasn1_modules==0.4.2
pycipher==0.5.2
pycparser==2.22
pydantic==2.11.4
pydantic-settings==2.9.1
pydantic_core==2.33.2
pydeck==0.9.1
Pygments==2.18.0
pyparsing==3.2.0
PyPDF2==3.0.1
python-dateutil==2.9.0.post0
python-dotenv==1.1.0
python-json-logger==3.3.0
python-multipart==0.0.20
python-slugify==8.0.4
pytz==2024.2
pywin32==308
pywinpty==2.0.15
PyYAML==6.0.2
pyzmq==26.2.0
referencing==0.36.2
regex==2024.11.6
requests==2.32.3
rfc3339-validator==0.1.4
rfc3986-validator==0.1.1
rich==13.9.3
rpds-py==0.24.0
rsa==4.9.1
scikit-learn==1.6.0
scipy==1.14.1
seaborn==0.13.2
Send2Trash==1.8.3
setuptools==75.2.0
shapely==2.1.0
six==1.16.0
smmap==5.0.2
sniffio==1.3.1
sounddevice==0.5.1
soupsieve==2.7
SQLAlchemy==1.4.54
sse-starlette==2.3.4
stack-data==0.6.3
starlette==0.46.2
streamlit==1.45.1
tenacity==9.1.2
tensorboard==2.19.0
tensorboard-data-server==0.7.2
tensorflow==2.19.0
tensorflow_intel==2.18.0
termcolor==2.5.0
terminado==0.18.1
text-unidecode==1.3
tf_keras==2.19.0
threadpoolctl==3.5.0
tiktoken==0.9.0
tinycss2==1.4.0
tokenizers==0.21.1
toml==0.10.2
tornado==6.4.1
tqdm==4.66.5
traitlets==5.14.3
types-python-dateutil==2.9.0.20250516
typing==3.7.4.3
typing-inspection==0.4.0
typing_extensions==4.12.2
tzdata==2024.2
tzlocal==5.3.1
uri-template==1.3.0
uritemplate==4.1.1
urllib3==2.2.3
utils==1.0.2
uvicorn==0.34.2
watchdog==6.0.0
wcwidth==0.2.13
webcolors==24.11.1
webencodings==0.5.1
websocket-client==1.8.0
websockets==15.0.1
Werkzeug==3.0.6
wheel==0.44.0
widgetsnbextension==4.0.14
wrapt==1.16.0
yarl==1.20.0
yfinance==0.2.56
zipp==3.21.0
transformers
torch
huggingface_hub
python-dotenv
transformers
torch
huggingface_hub
python-dotenv



we can use various trained model in the flashcard generation 
for example for openai gpt 3.5 model , we have first pay for using this model then
#(OpenAI) 
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
)

for example using huggingface models such as Llama-2-7b-chat-hf, mistralai/Mistral-7B-Instruct-v0.1"
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(
    "meta-llama/Llama-2-7b-chat-hf",
    use_auth_token="your_huggingface_token_here"
)
and in cmd pass command to authorize your model access
huggingface-cli login
transformers-cli repo info meta-llama/Llama-2-7b-chat-hf
for example using LLM 
To run locally:

    Request access here (for weights): https://ai.meta.com/resources/models-and-libraries/llama-downloads/

    Once granted, download the weights and convert them using tools like:

        transformers (from Hugging Face)

        llama.cpp (for CPU inference)

        Text Generation Web UI (GUI for chat-style interaction)

NOTE:- You need to have login credentials for each of the above options 




📄 License

This project is licensed under the MIT License. See LICENSE for details.

—

Let me know if you'd like the README customized for your GitHub profile, your tool name, or to include screenshots or demo links.
