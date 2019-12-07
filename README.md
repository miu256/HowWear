# HowWear

「昨日は寒かったから厚着で来たけど、今日は暑かった...」、「予報では暑いと言っているけど、実際に外出すると肌寒かった...」といった経験をしたことはありませんか？  
<br>
HowWearは、気温変化の激しい今日において、着ていく服に悩むあなたをサポートします。  
<br>
まずは、あなたが今日厚着で外出するか、薄着で外出するかどうかを投票してみましょう。  
投票後に、他の皆がどうであるのかを確認することができ、より良い決断を下すことができるでしょう。  
<br>

![HowWearGif](https://user-images.githubusercontent.com/48997441/61196959-10d02280-a70d-11e9-80b0-3365707d127a.gif)  
<br>
<br>


### Dependency  
* Python 3.6.8  
* pip 18.1  
* Django 2.2.8  
<br>

### 環境構築手順  
venvなどによる仮想環境上で、pipを用いてDjangoをインストールします。
```bash
python -m venv [name]
source [name]/bin/activate
pip install django
```  
<br>

### ローカル環境におけるWebサーバー立ち上げ手順  
フォルダを置く適当なディレクトリに移動し、以下を実行します。  
```bash
git clone https://github.com/miu256/HowWear.git
cd HowWear
python manage.py runserver
```  
無事Webサーバが立ち上がります。  
「You have unapplied migration」などと表示された場合は、念のために以下を実行してください。  
```bash
python manage.py migrate
```  
<br>

### テスト実行手順
以下を実行します。  
```bash
python manage.py test polls.tests
```  
<br>

### Author  
Rita Gunji
