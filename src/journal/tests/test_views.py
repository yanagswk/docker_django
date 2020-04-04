from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

from ..models import Journal


class LoggedInTestCase(TestCase):
    """各テストクラスで共通の事前準備処理をオーバーライドした独自TestCaseクラス"""

    def setUp(self):
        """テストメソッド実行前の事前設定"""

        # テストユーザーのパスワード
        self.password = 'qweasdqwe'

        # 各インスタンスメソッドで使うテスト用ユーザーを生成し
        # インスタンス変数に格納しておく
        self.test_user = get_user_model().objects.create_user(
            username='admins',
            email='yanagisawa3939jp@yahoo.co.jkp',
            password=self.password)

        # テスト用ユーザーでログインする
        self.client.login(email=self.test_user.email, password=self.password)


class TestDiaryCreateView(LoggedInTestCase):
    """DiaryCreateView用のテストクラス"""

    def test_create_diary_success(self):
        """日記作成処理が成功することを検証する"""

        # Postパラメータ
        params = {'title': 'テストタイトル',
                  'category': '本文',
                  'tags': '',
                  'content': '',
                  'photo3': '',
                  'picture1': '',
                  'picture2': '',
                  'picture3': ''}

        # 新規日記作成処理(Post)を実行
        response = self.client.post(reverse_lazy('journal:diary_create'), params)

        # 日記リストページへのリダイレクトを検証
        self.assertRedirects(response, reverse_lazy('journal:diary_list'))

        # 日記データがDBに登録されたかを検証
        self.assertEqual(Journal.objects.filter(title='テストタイトル').count(), 1)

    def test_create_diary_failure(self):
        """新規日記作成処理が失敗することを検証する"""

        # 新規日記作成処理(Post)を実行
        response = self.client.post(reverse_lazy('journal:diary_create'))

        # 必須フォームフィールドが未入力によりエラーになることを検証
        self.assertFormError(response, 'form', 'title', 'このフィールドは必須です。')


