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
        <a href="https://imgbb.com/"><img src="https://i.ibb.co/p1GWd8p/artificial-intelligence-humanoid-head-with-neural-network-thinks-futuristic-modern-3d-illustration-7.jpg" alt="artificial-intelligence-humanoid-head-with-neural-network-thinks-futuristic-modern-3d-illustration-7" border="0"></a>
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <a href="https://ibb.co/FnmFBLw"><img src="https://i.ibb.co/x3XNMtj/1000-F-217452019-c-Dxhxn2vh-Pbj-JX2wxl-Oh-Vl9-X3s-Yy2i5-U.jpg" alt="1000-F-217452019-c-Dxhxn2vh-Pbj-JX2wxl-Oh-Vl9-X3s-Yy2i5-U" border="0"></a>
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''