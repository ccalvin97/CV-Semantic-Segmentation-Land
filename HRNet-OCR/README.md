# High-resolution networks (HRNets) for Semantic Segmentation
## Branches
- This is the implementation for HRNet + OCR.
- The PyTroch 1.1 version ia available [here](https://github.com/HRNet/HRNet-Semantic-Segmentation/tree/pytorch-v1.1).
- The PyTroch 0.4.1 version is available [here](https://github.com/HRNet/HRNet-Semantic-Segmentation/tree/master).

## Research Paper  
**HRNet: https://arxiv.org/abs/1904.04514**    
**HRNet: https://arxiv.org/pdf/1908.07919.pdf**  
**OCR: https://arxiv.org/pdf/1909.11065.pdf**  

## Contribution  
Edited by kuancalvin2016@gmail.com  
Original Code from HRNet-OCR Official Github  



## Introduction

### Backbone
<!-- ![](figures/seg-hrnet.png) -->
<figure>
  <text-align: center;>
  <img src="https://github.com/ccalvin97/CV-Semantic-Segmentation-Land/blob/main/graph/Picture1.jpg" height="400" />
</figcaption>
</figure>

### OCR   
<figure>
  <text-align: center;>
  <img src="https://github.com/ccalvin97/CV-Semantic-Segmentation-Land/blob/main/graph/Picture3.png" height="200" />
</figcaption>
</figure>
<figure>
  <text-align: center;>
  <img src="https://github.com/ccalvin97/CV-Semantic-Segmentation-Land/blob/main/graph/Picture2.png" width="900" height="200" />
</figure>

## Pre-train Models  


| model | Train Set | Test Set | OHEM | Multi-scale| Flip | mIoU | Link |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| HRNetV2-W48 | Train | Val | No | No | No | 80.9 | [Github](https://github.com/hsfzxjy/models.storage/releases/download/HRNet-OCR/hrnet_cs_8090_torch11.pth)/[BaiduYun(Access Code:pmix)](https://pan.baidu.com/s/1KyiOUOR0SYxKtJfIlD5o-w)|
| HRNetV2-W48 + OCR | Train | Val | No | No | No | 81.6 | [Github](https://github.com/hsfzxjy/models.storage/releases/download/HRNet-OCR/hrnet_ocr_cs_8162_torch11.pth)/[BaiduYun(Access Code:fa6i)](https://pan.baidu.com/s/1BGNt4Xmx3yfXUS8yjde0hQ)|
| HRNetV2-W48 + OCR | Train + Val | Test | No | Yes | Yes | 82.3 | [Github](https://github.com/hsfzxjy/models.storage/releases/download/HRNet-OCR/hrnet_ocr_cs_trainval_8227_torch11.pth)/[BaiduYun(Access Code:ycrk)](https://pan.baidu.com/s/16mD81UnGzjUBD-haDQfzIQ)|

## Environments   

Computer - Standard NC6s_v3    
OS - Ubuntu 18.04  
conda environment - py37_pytorch  
CUDNN - 7.6.5  
CUDA - 10.1.243  
adal                         1.2.5  
alembic                      1.5.2  
anyio                        2.0.2  
applicationinsights          0.11.9  
argon2-cffi                  20.1.0  
async-generator              1.10  
attrs                        20.3.0  
azure-common                 1.1.26  
azure-graphrbac              0.61.1  
azure-mgmt-authorization     0.61.0  
azure-mgmt-containerregistry 2.8.0  
azure-mgmt-keyvault          2.2.0  
azure-mgmt-resource          12.0.0  
azure-mgmt-storage           11.2.0  
azureml-core                 1.20.0  
azureml-telemetry            1.20.0  
azureml-widgets              1.20.0  
Babel                        2.9.0  
backcall                     0.2.0  
backports.tempfile           1.0  
backports.weakref            1.0.post1  
bleach                       3.2.2  
brotlipy                     0.7.0  
certifi                      2020.12.5  
certipy                      0.1.3  
cffi                         1.14.4  
chardet                      4.0.0  
conda                        4.9.2  
conda-package-handling       1.7.2  
contextlib2                  0.6.0.post1  
cryptography                 3.3.1  
decorator                    4.4.2  
defusedxml                   0.6.0  
docker                       4.4.1  
entrypoints                  0.3  
idna                         2.10    
importlib-metadata           2.0.0  
ipykernel                    5.3.4  
ipython                      7.19.0  
ipython-genutils             0.2.0  
ipywidgets                   7.6.3  
isodate                      0.6.0  
jedi                         0.18.0  
jeepney                      0.6.0  
Jinja2                       2.11.2  
jmespath                     0.10.0  
Mako                         1.1.4  
MarkupSafe                   1.1.1  
mistune                      0.8.4  
msrest                       0.6.19  
msrestazure                  0.6.4  
nb-conda-kernels             2.3.1  
nbclassic                    0.2.6  
nbclient                     0.5.1  
nbconvert                    6.0.7  
nbformat                     5.1.2  
ndg-httpsclient              0.5.1  
nest-asyncio                 1.4.3  
notebook                     6.2.0  
oauthlib                     3.1.0  
packaging                    20.8  
pamela                       1.0.0  
pandocfilters                1.4.3  
parso                        0.8.1  
pathspec                     0.8.1  
pexpect                      4.8.0  
pickleshare                  0.7.5  
pip                          20.3.3  
prometheus-client            0.9.0  
prompt-toolkit               3.0.11  
psutil                       5.8.0  
ptyprocess                   0.7.0  
pyasn1                       0.4.8  
pycosat                      0.6.3  
pycparser                    2.20  
Pygments                     2.7.4  
PyJWT                        1.7.1  
pyOpenSSL                    19.1.0  
pyparsing                    2.4.7  
pyrsistent                   0.17.3  
PySocks                      1.7.1  
python-dateutil              2.8.1  
python-editor                1.0.4  
python-json-logger           2.0.1  
pytz                         2020.5  
pyzmq                        21.0.1  
requests                     2.25.1  
requests-oauthlib            1.3.0  
ruamel-yaml                  0.15.87  
ruamel.yaml                  0.16.12  
ruamel.yaml.clib             0.2.2  
SecretStorage                3.3.0  
Send2Trash                   1.5.0  
setuptools                   51.3.3.post20210118  
six                          1.15.0  
sniffio                      1.2.0  
SQLAlchemy                   1.3.22  
sudospawner                  0.6.0.dev0  
terminado                    0.9.2  
testpath                     0.4.4  
tornado                      6.1  
tqdm                         4.55.1  
traitlets                    5.0.5  
urllib3                      1.26.2  
wcwidth                      0.2.5  
webencodings                 0.5.1    
websocket-client             0.57.0  
wheel                        0.36.2  
widgetsnbextension           3.5.1  
zipp                         3.4.0  




## Quick start
### Install
$ Install dependencies: pip install -r requirements.txt


### Data preparation

Your directory tree should be look like this:
````bash
$SEG_ROOT/data
├── urbanisation
│   ├── x
│   │   ├── test
│   │   ├── train
│   │   └── val
│   └── y
│       ├── test
│       ├── train
│       └── val
````

### Train and Test
$ bash train_start.sh  
$ bash est_start.sh   
  

## Citation
If you find this work or code is helpful in your research, please cite:
````
@inproceedings{SunXLW19,
  title={Deep High-Resolution Representation Learning for Human Pose Estimation},
  author={Ke Sun and Bin Xiao and Dong Liu and Jingdong Wang},
  booktitle={CVPR},
  year={2019}
}

@article{WangSCJDZLMTWLX19,
  title={Deep High-Resolution Representation Learning for Visual Recognition},
  author={Jingdong Wang and Ke Sun and Tianheng Cheng and 
          Borui Jiang and Chaorui Deng and Yang Zhao and Dong Liu and Yadong Mu and 
          Mingkui Tan and Xinggang Wang and Wenyu Liu and Bin Xiao},
  journal={TPAMI},
  year={2019}
}

@article{YuanCW19,
  title={Object-Contextual Representations for Semantic Segmentation},
  author={Yuhui Yuan and Xilin Chen and Jingdong Wang},
  booktitle={ECCV},
  year={2020}
}
````

## Acknowledgement
We adopt sync-bn implemented by [InplaceABN](https://github.com/mapillary/inplace_abn) for PyTorch 0.4.1 experiments and the official 
sync-bn provided by PyTorch for PyTorch 1.10 experiments.

We adopt data precosessing on the PASCAL-Context dataset, implemented by [PASCAL API](https://github.com/zhanghang1989/detail-api).
