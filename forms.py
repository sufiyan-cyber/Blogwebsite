
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField
from wtforms.validators import DataRequired, URL, Length
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class Createregistrationform(FlaskForm):
    email=StringField("your email",validators=[DataRequired()])
    password=PasswordField("your password",validators=[DataRequired()])
    name=StringField("your name",validators=[DataRequired()])
    submit=SubmitField("submit form")




class Loginform(FlaskForm):
    email=StringField("your email",validators=[DataRequired()])
    password=PasswordField("your password",validators=[DataRequired()])
    submit=SubmitField("submit form")


# CommentForm for users to leave comments below posts
class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired(), Length(max=500)])
    submit = SubmitField("Submit Comment")
