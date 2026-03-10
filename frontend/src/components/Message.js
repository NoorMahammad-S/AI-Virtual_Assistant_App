import React from "react";

function Message({ sender, text }) {
  return (
    <div className={sender === "user" ? "userMessage" : "botMessage"}>
      {text}
    </div>
  );
}

export default Message;