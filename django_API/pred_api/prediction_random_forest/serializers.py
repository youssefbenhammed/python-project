from rest_framework import serializers
from prediction_random_forest.models import Activity


class ActivitySerializer(serializers.Serializer)  :
    """ to serialize or deserialize data
    -> Serialize                               : model instance / querysets => native Python datatypes => JSON
        ** NETWORK **
    -> Deserialize                             : JSON to model instance
    """

    #Dependent Variable y
    activity        =serializers.FloatField(allow_null=True)
    #Variable X
    respiration     =serializers.FloatField()
    ECG             =serializers.FloatField()
    ACC_c_x         =serializers.FloatField()
    ACC_c_y         =serializers.FloatField()
    ACC_c_z         =serializers.FloatField()
    ACC_w_x         =serializers.FloatField()
    ACC_w_y         =serializers.FloatField()
    ACC_w_z         =serializers.FloatField()
    temperature     =serializers.FloatField()
    EDA             =serializers.FloatField()
    BVP             =serializers.FloatField()
    WEIGHT          =serializers.FloatField()
    Gender          =serializers.FloatField()
    AGE             =serializers.FloatField()
    SKIN            =serializers.FloatField()
    HEIGHT          =serializers.FloatField()
    SPORT           =serializers.FloatField()
    label           =serializers.FloatField()


    

    def create(self, validated_data)           :
        """ Create and return a new 'Incident' instance, given the validated data """
        return Activity.objects.create(**validated_data)

    def update(self, instance, validated_data) :
        """ Update and return an existing 'Houste' instance, given the validated data """
        instance.respiration            =validated_data.get('respiration',instance.respiration)
        instance.ECG                    =validated_data.get('ECG',instance.ECG)
        instance.ACC_c_x                =validated_data.get('ACC_c_x',instance.ACC_c_x)
        instance.ACC_c_y                =validated_data.get('ACC_c_y',instance.ACC_c_y)
        instance.ACC_c_z                =validated_data.get('ACC_c_z',instance.ACC_c_z)
        instance.ACC_w_x                =validated_data.get('ACC_w_x',instance.ACC_w_x)
        instance.ACC_w_y                =validated_data.get('ACC_w_y',instance.ACC_w_y)
        instance.ACC_w_z                =validated_data.get('ACC_w_z',instance.ACC_w_z)
        instance.temperature =validated_data.get('temperature', instance.temperature)    
        instance.EDA         =validated_data.get('EDA',         instance.EDA)       
        instance.BVP         =validated_data.get('BVP',         instance.BVP)      
        instance.WEIGHT      =validated_data.get('WEIGHT',      instance.WEIGHT )      
        instance.Gender      =validated_data.get('Gender',      instance.Gender )       
        instance.AGE         =validated_data.get('AGE',         instance.AGE  )       
        instance.SKIN        =validated_data.get('SKIN',        instance.SKIN ) 
        instance.HEIGHT      =validated_data.get('HEIGHT',      instance.HEIGHT )     
        instance.SPORT       =validated_data.get('SPORT',       instance.SPORT)        
        instance.label       =validated_data.get('label',       instance.label)          

        #instance.MEDV   = validated_data.get('MEDV' , instance.MEDV)
        instance.save()
        return instance
