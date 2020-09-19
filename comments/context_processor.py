from .models import Comment
def add_to_base(request):
    return {
        'comment_from_processor' : Comment.objects.filter(parent=None),
        'reply_from_processor': Comment.objects.all().exclude(parent=None),
    }