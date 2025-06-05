import React, { useState } from "react";

export default function App() {
  const [input, setInput] = useState("");
  const [chatLog, setChatLog] = useState([]);
  const [topic, setTopic] = useState("");

  const handleTopicChange = async (e) => {
    const selected = e.target.value;
    setTopic(selected);
    if (selected !== "") {
      const prompt = `Let's practice a conversation about "${selected}". Please speak simple English and correct me if I make mistakes.`;

      const res = await fetch("https://english-learning-assistant.onrender.com/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: prompt })
      });
      const data = await res.json();
      setChatLog([...chatLog, { user: `🧠 Topic: ${selected}`, ai: data.reply }]);
    }
  };

  const sendMessage = async () => {
    const res = await fetch("https://english-learning-assistant.onrender.com/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ message: input })
    });
    const data = await res.json();
    setChatLog([...chatLog, { user: input, ai: data.reply }]);
    setInput("");
  };

  return (
    <div className="min-h-screen bg-gray-100 p-4">
      <div className="max-w-2xl mx-auto bg-white rounded-2xl shadow-lg p-6">
        <h1 className="text-2xl font-bold text-center mb-4">📚 英文學習助手</h1>

        <div className="mb-4">
          <label className="block mb-1 font-semibold text-gray-700">🎯 選擇學習主題</label>
          <select
            value={topic}
            onChange={handleTopicChange}
            className="w-full p-2 border rounded"
          >
            <option value="">-- 請選擇主題 --</option>
            <option value="Self Introduction">自我介紹</option>
            <option value="Ordering Food">餐廳點餐</option>
            <option value="Travel Conversation">旅行對話</option>
            <option value="Job Interview">工作面試</option>
          </select>
        </div>

        <div className="space-y-4 mb-6 max-h-96 overflow-y-auto border p-4 rounded bg-gray-50">
          {chatLog.map((entry, i) => (
            <div key={i} className="text-sm">
              <p><span className="font-semibold text-blue-600">You:</span> {entry.user}</p>
              <p><span className="font-semibold text-green-600">AI:</span> {entry.ai}</p>
            </div>
          ))}
        </div>

        <div className="flex gap-2">
          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            className="flex-grow border rounded px-3 py-2"
            placeholder="Type your English sentence here..."
          />
          <button
            onClick={sendMessage}
            className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
          >
            Send
          </button>
        </div>
      </div>
    </div>
  );
}
