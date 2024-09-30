import mongoengine as me


class PDFData(me.Document):
    email = me.EmailField(unique=True, require=True)
    extracted_nouns = me.ListField(me.StringField())
    extracted_verbs = me.ListField(me.StringField())
    pdf_name = me.StringField()
    created_at = me.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pdf_name
