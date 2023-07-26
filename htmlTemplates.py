css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.freepik.com%2Fpremium-photo%2Fartificial-intelligence-humanoid-head-with-neural-network-thinks-futuristic-modern-3d-illustration_34824715.htm&psig=AOvVaw0c8ZSpmeCl29AG399bp79n&ust=1690420956728000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCNiql_eaq4ADFQAAAAAdAAAAABAE" alt="">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="PDF-Chat\img\smiley.png" alt="">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''