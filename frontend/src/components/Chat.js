import React, { useState } from "react";
import Message from "./Message";
import VoiceButton from "./VoiceButton";

function Chat() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = async (message) => {
    if (!message) return;

    const userMessage = { sender: "user", text: message };
    setMessages((prev) => [...prev, userMessage]);

    try {
      const res = await fetch("http://localhost:5000/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message }),
      });

      const data = await res.json();
      const botMessage = { sender: "bot", text: data.reply };
      setMessages((prev) => [...prev, botMessage]);
    } catch (err) {
      const botMessage = { sender: "bot", text: "Server error. Try again." };
      setMessages((prev) => [...prev, botMessage]);
    }
  };

  return (
    <div>
      <div className="chatBox">
        {messages.map((msg, i) => (
          <Message key={i} sender={msg.sender} text={msg.text} />
        ))}
      </div>

      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Type a message..."
        onKeyDown={(e) => e.key === "Enter" && (sendMessage(input), setInput(""))}
      />
      <button
        onClick={() => {
          sendMessage(input);
          setInput("");
        }}
      >
        Send
      </button>
      <VoiceButton sendMessage={sendMessage} />
    </div>
  );
}

export default Chat;