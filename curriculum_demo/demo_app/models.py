from curriculum.models.resume import AbstractUserResumes


class UserResumes(AbstractUserResumes):
    class Meta:
        app_label = 'demo_app'
