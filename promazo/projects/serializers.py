from rest_framework import serializers

class projectRoleSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    roleType = serializers.StringRelatedField(many=True)
    numHours = serializers.IntegerField()

class projectPlaceSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    projectRole = serializers.StringRelatedField(many=True)
    userStartDate = serializers.DateField()
    endDate = serializers.DateField()
    status = serializers.CharField(max_length=50)
    numHours = serializers.IntegerField()
    notes = serializers.CharField()

'''
#Project Place
class projectPlaces(baseModel):
    name = models.CharField(max_length=200)
    projectRole = models.ManyToManyField(projectRoles,related_name="Is_a_part")
    userStartDate = models.DateField(auto_now=True,auto_now_add=False)
    endDate = models.DateField()
    #Setup Status options
    status = models.CharField(
        max_length = 50,
        choices = (
            ('Inactive','Inactive'),
            ('Active','Active')
        ),
        default='Active' #Upon creation, a place will probably be active
    )
    numHours = models.SmallIntegerField()
    notes = models.TextField()
'''
