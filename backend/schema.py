import graphene
import random
import uuid
from graphene_django import DjangoObjectType, DjangoListField
from .models import Posts, PostImage,Approval, Decline, Comment 
from graphql_auth.schema import UserQuery, MeQuery
from customuser.models import Account, UserImage
from customuser.schema import AuthMutation
from django.conf import settings


            
# class UserImageType(DjangoObjectType):
#     class Meta:
#         model = UserImage
#         fields = ("post", "image")
        
#         def resolve_image(self,info):
#             self.user_image = info.context.build_absolute_uri(self.image.url)
#             return settings.MEDIA_ROOT + self.user_image
            
class ApprovalType(DjangoObjectType):
    class Meta:
        model = Approval
        fields = ('post','user', 'Time', 'name')
        
class DeclineType(DjangoObjectType):
    class Meta:
        model = Decline
        fields = ('post','user', 'Time', 'name')
        
class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        fields = ('post','user', 'Time', 'name','Text')


class Connection(graphene.Connection):
    class Meta:
        abstract = True

    total_count = graphene.Int()

    def resolve_total_count(self, info):
        return self.length

class PostsType(DjangoObjectType):
    class Meta:
        model = Posts
        fields = ('PostId',
                  'uuid',
                  'Owner',
                  'PublishDate',
                  'Photo',
                  'Title',
                  'Text',
                  'Tags',
                  'Category',
                  'ObjectionTo',
                  'post_image',
                  'Approvals',
                  'Declines',
                  'Comments'
                  )
        interfaces = (graphene.relay.Node, )
        Approvals = graphene.Field(ApprovalType)
        Declines = graphene.Field(DeclineType)
        Comments = graphene.Field(CommentType)
        interfaces = (graphene.Node, )
        connection_class = Connection
   
        

        
        
class PostImageType(DjangoObjectType):
    class Meta:
        model = PostImage
        fields = ("post", "image")
        
    def resolve_post_image(self,info):
        if self.image:
            self.image = info.context.build_absolute_uri(self.image)
        return self.image
        
        
        
class AccountsType(DjangoObjectType):
    class Meta:
        model = Account
        fields = ('email',
                  'username',
                  'first_name',
                  'last_name',
                  'bio',
                  'photo',
                  'date_joined',
                  'last_login',
                  'is_admin',
                  'is_active',
                  'is_staff',
                  'is_superuser',
                  'user_image',
                  'Approvals',
                  'Declines',
                  'Comments')
        Approvals = graphene.Field(ApprovalType)
        Declines = graphene.Field(DeclineType)
        Comments = graphene.Field(CommentType)

    
class Query(UserQuery, MeQuery, graphene.ObjectType):
    
    accounts = graphene.Field(AccountsType, Username= graphene.String())
    random_post = graphene.Field(PostsType, uuid= graphene.String()) 
    posts = graphene.List(PostsType, Owner= graphene.String(), uuid= graphene.String())
    post_image = graphene.Field(PostImageType,)
    approval = graphene.Field(ApprovalType, name= graphene.String())
    decline = graphene.Field(DeclineType, name= graphene.String())

    node = graphene.Node.Field()
    
    def resolve_posts(root, info, **kwargs):
        Owner = kwargs.get('Owner')
        uuid = kwargs.get('uuid')
        
        if not Owner:
            return Posts.objects.all()
        return Posts.objects.filter(Owner__username= Owner)

    def resolve_random_post(root, info, **kwargs):
        uuid = kwargs.get('uuid')
        if uuid == "discover":
            length = len(Posts.objects.all())
            RandId = int(random.uniform(0, length))
            allPosts = Posts.objects.all()
            PostId = allPosts[RandId].PostId
            return Posts.objects.get(PostId= PostId)
        else:
            return Posts.objects.get(uuid=uuid)
    
    def resolve_accounts(root, info, **kwargs):
        Username = kwargs.get('Username')
        return Account.objects.get(username=Username)
    
    def resolve_approval(root,info, **kwargs):
        name = kwargs.get('name')
        try:
            Approval.objects.get(name=name)
            return Approval.objects.get(name=True)
        except:
            return Approval.objects.get(name=False)
        
    def resolve_decline(root,info, **kwargs):
        name = kwargs.get('name')
        try:
            print("BURDADA")
            Decline.objects.get(name=name)
            return Decline.objects.get(name=True)
        except:
            return Decline.objects.get(name=False)
    #  <--- SECOND WAY TO CREATE ENDPOINT --->
    # all_posts = graphene.List(PostsType)
    
    # def resolve_all_posts(root, info):
    #     return Posts.objects.all()
    
class OwnerInput(graphene.InputObjectType):
    email = graphene.String()
    username = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()
    date_joined = graphene.DateTime()
    last_login = graphene.DateTime()
    is_admin = graphene.Boolean()
    is_active = graphene.Boolean()
    is_staff = graphene.Boolean()
    is_superuser = graphene.Boolean()

class PostInput(graphene.InputObjectType):
    Owner = graphene.String()
    # PublishDate = graphene.DateTime()
    Title = graphene.String()
    Text = graphene.String()
    Photo = graphene.String()
    Tags = graphene.String()
    Category = graphene.String()
    ObjectionTo = graphene.UUID()
    
class AddPost(graphene.Mutation):
    post = graphene.Field(PostsType)
    
    class Arguments:
        post_data = PostInput(required= True)
    @staticmethod
    def mutate(root,info, post_data):
        owner_obj = Account.objects.get(username= post_data['Owner'])
        _post = Posts.objects.create(Owner= owner_obj,
                                    # PublishDate= post_data['PublishDate'],
                                    Title= post_data['Title'],
                                    Text= post_data['Text'],
                                    Photo= post_data['Photo'],
                                    Tags= post_data['Tags'],
                                    Category= post_data['Category'],
                                    ObjectionTo= post_data['ObjectionTo']
                                     )
        return AddPost(post=_post)

class RemovePost(graphene.Mutation):
    post = graphene.Field(PostsType)
    
    class Arguments:
        post_uuid = graphene.String(required= True)
        
    @staticmethod
    def mutate(root,info, post_uuid):
        post = Posts.objects.get(uuid= post_uuid)
        post.delete()
        return RemovePost(post=post)

class UpdatePost(graphene.Mutation):
    post = graphene.Field(PostsType)
    
    class Arguments:
        post_uuid = graphene.UUID(required= True)
        post_data = PostInput(required= True)
        
    @staticmethod
    def mutate(root, info, **kwargs):
        post_uuid = kwargs.get('post_uuid', None)
        post_data = kwargs.get('post_data', None)
        
        post = Posts.objects.get(uuid= post_uuid)
        if not post_data['Title'] == "": 
            post.Title = post_data['Title']
        if not post_data['Text'] == "": 
            post.Text = post_data['Text']
        if not post_data['Photo'] == "": 
            post.Photo = post_data['Photo']
        if not post_data['Tags'] == "": 
            post.Tags = post_data['Tags']
        if not post_data['Category'] == "": 
            post.Category = post_data['Category']
        post.save()
        return UpdatePost(post=post)
    
class addApproval(graphene.Mutation):
    approval = graphene.Field(ApprovalType)
    # decline = graphene.Field(DeclineType)
    
    class Arguments:
        post_uuid = graphene.String(required= True)
        username = graphene.String(required= True)
        
        
    @staticmethod
    def mutate(root, info, **kwargs):
   
        post_uuid = kwargs.get('post_uuid', None)
        username = kwargs.get('username', None)
        name = f'{post_uuid}+{username}'  
        
        post = Posts.objects.get(uuid= post_uuid)
        user = Account.objects.get(username= username)
        try:
            decline = Decline.objects.get(name=name)
            post.Declines.remove(decline)
            user.Declines.remove(decline)
            decline.delete()    
            approval = Approval(post=post, user=user, name= f'{post.uuid}+{username}')
            approval.save()
            post.Approvals.add(approval)
            user.Approvals.add(approval)
            return addApproval(Approval.objects.get(name= True))
        except:
            approval = Approval(post=post, user=user, name= f'{post.uuid}+{username}')
            approval.save()
            post.Approvals.add(approval)
            user.Approvals.add(approval)
            return addApproval(Approval.objects.get(name= True))
    
class removeApproval(graphene.Mutation):
    # approval = graphene.Field(ApprovalType)
    decline = graphene.Field(DeclineType)
        
    
    class Arguments:
        post_uuid = graphene.String(required= True)
        username = graphene.String(required= True)
        
        
    @staticmethod
    def mutate(root, info, **kwargs):
        post_uuid = kwargs.get('post_uuid', None)
        username = kwargs.get('username', None)
        name = f'{post_uuid}+{username}'  
        post = Posts.objects.get(uuid= post_uuid)
        user = Account.objects.get(username= username)
        
        try:
            approval = Approval.objects.get(name=name)
            post.Approvals.remove(approval)
            user.Approvals.remove(approval)
            approval.delete()
            decline = Decline(post=post, user=user, name= f'{post.uuid}+{username}')
            decline.save()
            post.Declines.add(decline)
            user.Declines.add(decline)
            return removeApproval(Decline.objects.get(name=True))
        except:
            decline = Decline(post=post, user=user, name= f'{post.uuid}+{username}')
            decline.save()
            post.Declines.add(decline)
            user.Declines.add(decline)
            return removeApproval(Decline.objects.get(name=True))
    
class addComment(graphene.Mutation):
    comment = graphene.Field(CommentType)
    
    class Arguments:
        post_uuid = graphene.String(required= True)
        username= graphene.String(required= True)
        Text= graphene.String(required= True)
        
    @staticmethod
    def mutate(root,info, **kwargs):
        post_uuid = kwargs.get('post_uuid', None)
        username = kwargs.get('username', None)
        Text= kwargs.get('Text',None)
        name = f'com+{post_uuid}+{username}'  
        post = Posts.objects.get(uuid= post_uuid)
        user = Account.objects.get(username= username)

        try:
            comment = Comment.objects.get(name=name)
            return addComment(Comment.objects.get(name=False))
        except:
            comment = Comment(post=post, user=user, Text=Text, name=name)
            comment.save()
            post.Comments.add(comment)
            user.Comments.add(comment)
            return addComment(comment)
        
class removeComment(graphene.Mutation):
    comment = graphene.Field(CommentType)
    
    class Arguments:
        name = graphene.String(required= True)
        
    @staticmethod
    def mutate(root,info, **kwargs):
        name = kwargs.get('name', None)
        varib = name.split('+')
        comment = Comment.objects.get(name=name)
        post = Posts.objects.get(uuid= varib[1])
        user = Account.objects.get(username= varib[2])
        
        post.Comments.remove(comment)
        user.Comments.remove(comment)
        comment.delete()
        return removeComment(Comment.objects.get(name=True))
        

class Mutation(AuthMutation, graphene.ObjectType):
    add_post = AddPost.Field()
    remove_post = RemovePost.Field()
    update_post = UpdatePost.Field()
    add_approval = addApproval.Field()
    remove_approval = removeApproval.Field()
    add_comment = addComment.Field()
    remove_comment = removeComment.Field()

schema = graphene.Schema(query= Query, mutation= Mutation)