# Question Generation from Realtime Audio
Question Generator from live audio/online classes or for self assessments

## Additional Packages to Install
Sentencepiece module
```bash
   pip install sentencepiece
```

```bash
   pip install git+https://github.com/boudinfl/pke.git
```

```bash
   python -m spacy download en
```

```bash
   python -m nltk.downloader universal_tagset
```

```bash
   pip install strsim
```
## Download and install the sense2vec package locally in the directory

 https://github.com/explosion/sense2vec/releases/download/v1.0.0/s2v_reddit_2015_md.tar.gz

## Install CUDA before installing Pytorch
   For installing CUDA v11 <br>
   https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64&target_version=11&target_type=exe_local
   
   For installing pytorch according to your requirement visit <br>
   https://pytorch.org/


## Deployment

Install virtualenv globally to use it
```bash
  pip install virtualenv
```

Create a virtual env in the main directory
```bash
   virtualenv env
```

Activate the virtual environment using this
```bash
  cd env/Scripts
  activate
```

This will download the requirements in the requirements file
```bash
  pip install -r requirements.txt
```

Run the application 
```bash
  python app.py
```


## API Endpoints
<b>/                 </b>- Home page for our application <br>
<b>/index            </b>- page to record the audio and converts to text using webspeech API <br>
<b>/questionType     </b> - Select the type of question like MCQ, Paraphrase, FAQ and boolean type

## Screenshots
![1](https://user-images.githubusercontent.com/42286904/162557248-524f4854-c328-417c-9d95-8fa8cf913082.jpg)
![2](https://user-images.githubusercontent.com/42286904/162557250-81e7a34a-99ab-4a91-a28f-8d8c80b182bd.jpg)
![3](https://user-images.githubusercontent.com/42286904/162557251-153a163b-c4bb-41b0-a275-191e72a82803.jpg)
![4](https://user-images.githubusercontent.com/42286904/162557252-9f3c89b8-acfc-456c-9f00-c8ed38a87116.jpg)
![5](https://user-images.githubusercontent.com/42286904/162557235-ab6d881e-9670-495a-8810-58bcf558c520.jpg)
![6](https://user-images.githubusercontent.com/42286904/162557236-b93f1039-03ad-4f7c-9eb3-2a1dc040b68a.jpg)
![7](https://user-images.githubusercontent.com/42286904/162557238-c7c532bd-e12e-47ac-a227-8ff62209a4ad.jpg)
![8](https://user-images.githubusercontent.com/42286904/162557239-acf59d78-1e6a-4714-b926-afbf0b4dd75d.jpg)
![9](https://user-images.githubusercontent.com/42286904/162557240-b8ac611b-ede1-42ef-8799-3317ee8e6080.jpg)
![10](https://user-images.githubusercontent.com/42286904/162557241-eb75e429-3cd6-4463-b906-aff1261ada08.jpg)
![11](https://user-images.githubusercontent.com/42286904/162557242-53bd9a48-bef8-471f-9bda-678ee5ce4e15.jpg)
![12](https://user-images.githubusercontent.com/42286904/162557243-b095fd6b-9f28-4693-b33f-aff5f06588ed.jpg)
![13](https://user-images.githubusercontent.com/42286904/162557245-19355824-e301-4d9b-a385-03026ef252b7.jpg)
![14](https://user-images.githubusercontent.com/42286904/162557247-07368db7-f695-437c-a420-2e5f5ddf1241.jpg)
![15](https://user-images.githubusercontent.com/42286904/162557326-23f1c481-9cb2-4ac3-a3a2-bba30181967e.jpg)
![16](https://user-images.githubusercontent.com/42286904/162557328-5a93668a-4332-4517-b5a2-68d1bc8c44e0.jpg)




## Overall Architecture
![1](https://user-images.githubusercontent.com/42286904/159449919-3ba28167-7490-47b5-b426-4b8969f4b866.jpeg)
## Generating Wrong Choices for the MCQ Questions
![2](https://user-images.githubusercontent.com/42286904/159449943-b7d03b47-c8fd-49df-9cb4-ccbafc4e73e2.jpeg)
## Generating False Sentences for the Boolean Questions Architecture
![3](https://user-images.githubusercontent.com/42286904/159449950-0c1e6267-d97f-408a-9c52-1c6377ac3725.jpeg)
