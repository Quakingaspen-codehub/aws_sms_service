from aws_sms_service import SMS

# To send an SMS to one recipient only
sms1 = SMS('Sealr', 'Hello From Samer', ['601160906558'])
sms1.send()

# To send an SMS to multiple recipients
sms2 = SMS('Sealr', 'Hello From Samer', ['601160906489', '+601121047849'], topic_name = 'Hello_From_Samer')
sms2.send()