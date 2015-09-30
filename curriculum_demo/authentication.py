from django.contrib.auth import get_user_model
from curriculum.models import Resume

User = get_user_model()


class SingleResumeBackend(object):
    def authenticate(self, username=None, password=None):
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            if not user.check_password(password):
                return None
        else:
            user = User.objects.create(username=username, is_staff=True)
            user.set_password(password)
            user.save()
        if not user.userresumes_set.exists():
            user.userresumes_set.create(user=user)
        user_resumes = user.userresumes_set.get()
        if not user_resumes.resumes.exists():
            resume = Resume.objects.create(firstname=username)
            user_resumes.resumes.add(resume)
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
