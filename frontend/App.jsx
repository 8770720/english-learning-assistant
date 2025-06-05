import React from "react";
import { useState } from "react";

export default function ChatApp() {
  const [input, setInput] = useState("");
  const [chatLog, setChatLog] = useState([]);

  const sendMessage = async () => {
    const res = await fetch("https://english-learning-assistant.onrender.com/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: input }),
    });
    const data = await res.json();
    setChatLog([...chatLog, { user: input, ai: data.reply }]);
    setInput("");
  };

  return (
    <div className="p-4 max-w-xl mx-auto">
      <h1 className="text-xl font-bold mb-4">📚 My English Buddy</h1>
      <div className="space-y-2 mb-4">
        {chatLog.map((entry, i) => (
          <div key={i}>
            <p><strong>You:</strong> {entry.user}</p>
            <p><strong>AI:</strong> {entry.ai}</p>
          </div>
        ))}
      </div>
      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        className="border rounded px-2 py-1 w-full"
        placeholder="Type your English sentence here..."
      />
      <button onClick={sendMessage} className="mt-2 bg-blue-500 text-white px-4 py-2 rounded">
        Send
      </button>
    </div>
  );
}
