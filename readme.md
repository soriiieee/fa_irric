#install 

pip install email_validator


# create_app を作成する

--APPNAME
    /templates
        home.jinja
        welcome.jinja

    __init__.py : ココにcreate_app()に関する情報を設定してく
    
    forms.py
    models.py
    views.py: ここにblueprintに関する情報を設定していく

setup.py
    from APPNAME import create_app (APPNAMEが読み出されたタイミングで、create_appも呼ばれるため)

# ターミナルでmigrationの実施
* $cd APPNAME
* $set FLASK_APP=setup.py

* flask db init (一番最初の初期化の設定)
* flask db migrate - m "init migration"
* flask db upgrade






