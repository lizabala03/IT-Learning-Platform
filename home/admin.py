from django.contrib import admin

# Register your models here.
from .models import User, Profile
from .models import User, Course
from .models import User, Payment
from .models import User, Quiz
from .models import User, Dashboard
from .models import User, Certificate
from .models import User, Contact

admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(Payment)
admin.site.register(Quiz)
admin.site.register(Dashboard)
admin.site.register(Certificate)
admin.site.register(Contact)
