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


## Screenshots
![1](https://user-images.githubusercontent.com/42286904/159449716-c8c0ae42-1954-432c-8f0d-6fa08bd54b26.jpeg)
![2](https://user-images.githubusercontent.com/42286904/159449734-6fa1698e-4ad0-443d-a532-0e20b492d4db.jpeg)
![3](https://user-images.githubusercontent.com/42286904/159449739-a9855e43-5f98-406d-bb90-0d86931c77e8.jpeg)
![4](https://user-images.githubusercontent.com/42286904/159449741-330ef623-bfb2-4c28-917a-8dd166942d89.jpeg)
![5](https://user-images.githubusercontent.com/42286904/159449747-5926caee-53cb-4593-ac67-83a13d51db9b.jpeg)
![6](https://user-images.githubusercontent.com/42286904/159449749-f0d6373b-4027-45b8-bb60-8e7e1eaf6ea2.jpeg)

![7](https://user-images.githubusercontent.com/42286904/161430885-965e0479-7cf0-4448-92a5-7b649eab7e56.jpeg)

![8](https://user-images.githubusercontent.com/42286904/161430917-16e95298-8029-4b0c-92da-9c10dc61c557.jpg)
![9](https://user-images.githubusercontent.com/42286904/161430939-ee6d02da-d496-4498-b067-04b8af4a419d.jpg)
![10](https://user-images.githubusercontent.com/42286904/161430946-f44eac76-bb3f-4af5-a18a-38b709cda58f.jpg)
![11](https://user-images.githubusercontent.com/42286904/161430957-3bb1435b-5fbd-4ebb-ae07-2a657ccaa3a7.jpg)
![12](https://user-images.githubusercontent.com/42286904/161430962-ea029969-ae19-4292-98b9-71cfb0fafd66.jpg)



## Overall Architecture
![1](https://user-images.githubusercontent.com/42286904/159449919-3ba28167-7490-47b5-b426-4b8969f4b866.jpeg)
## Generating Wrong Choices for the MCQ Questions
![2](https://user-images.githubusercontent.com/42286904/159449943-b7d03b47-c8fd-49df-9cb4-ccbafc4e73e2.jpeg)
## Generating False Sentences for the Boolean Questions Architecture
![3](https://user-images.githubusercontent.com/42286904/159449950-0c1e6267-d97f-408a-9c52-1c6377ac3725.jpeg)
