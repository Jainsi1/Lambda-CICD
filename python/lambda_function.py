import boto3
import yaml
client = boto3.client('iam')
module.exports = {
  showMessage: python() {
def lambda_handler():
 
  with open('data.yaml') as f:
         data = yaml.load(f,Loader= yaml.FullLoader)

  userlist = data['Users']
  for users in userlist: 
      print(users)     
      response = client.create_user(
      UserName=users
       )
      print(response)

  grouplist = data['GroupAssignment']     
  for groups in grouplist:
      print (groups)
      group = client.create_group(
      GroupName=groups
       )
      print (group)
      for x in grouplist[groups]:

          usergroup = client.add_user_to_group(
          GroupName=groups,
          UserName=x
          )      
        
          print (usergroup)
  }
