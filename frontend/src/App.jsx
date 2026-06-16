import { useState } from "react";

function App() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const askQuestion = async () => {
    if (!question.trim()) return;

    const userMessage = {
      role: "user",
      content: question,
    };

    setMessages((prev) => [...prev, userMessage]);

    setLoading(true);

    try {
      const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question,
        }),
      });

      const data = await response.json();

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: data.answer,
        },
      ]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: "Something went wrong.",
        },
      ]);
    }

    setQuestion("");
    setLoading(false);
  };

  return (
    <div className="h-screen flex flex-col bg-black text-white">
      <div className="flex-1 overflow-y-auto p-4 max-w-4xl mx-auto w-full">
        {messages.length === 0 && (
          <div className="h-full flex items-center justify-center">
            <h1 className="text-2xl md:text-4xl font-bold text-center">
              Ask Vyas AI
            </h1>
          </div>
        )}

        {messages.map((msg, index) => (
          <div
            key={index}
            className={`mb-4 flex ${
              msg.role === "user" ? "justify-end" : "justify-start"
            }`}
          >
            <div
              className={`max-w-[85%] md:max-w-[70%] rounded-2xl px-4 py-3 whitespace-pre-wrap ${
                msg.role === "user" ? "bg-blue-600" : "bg-zinc-800"
              }`}
            >
              {msg.content}
            </div>
          </div>
        ))}

        {loading && (
          <div className="bg-zinc-800 inline-block px-4 py-3 rounded-2xl">
            Thinking...
          </div>
        )}
      </div>

      <div className="border-t border-zinc-800 p-4">
        <div className="max-w-4xl mx-auto flex gap-2">
          <input
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && askQuestion()}
            placeholder="Ask anything..."
            className="flex-1 bg-zinc-900 rounded-xl px-4 py-3 outline-none"
          />

          <button
            onClick={askQuestion}
            className="bg-white text-black px-5 rounded-xl font-semibold"
          >
            Send
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;
