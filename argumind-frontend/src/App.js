import React, { useState } from "react";
import FlowView from "./FlowView";
import { runDebate } from "./api";

function App() {
  const [topic, setTopic] = useState("");
  const [rounds, setRounds] = useState(3);
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  const startDebate = async () => {
    if (!topic) {
      alert("Please enter a topic");
      return;
    }
    setLoading(true);
    const result = await runDebate(topic, rounds);
    setData(result);
    setLoading(false);
  };

  return (
    <div style={{ background: "#020617", color: "white", minHeight: "100vh", padding: 20 }}>
      <h1 style={{ fontSize: 28 }}>🧠 ArguMind – Multi-Agent Debate System</h1>

      <div style={{ margin: "20px 0" }}>
        <input
          placeholder="Enter debate topic"
          value={topic}
          onChange={(e) => setTopic(e.target.value)}
          style={{
            padding: 10,
            width: 350,
            marginRight: 10,
            borderRadius: 6,
            border: "none",
          }}
        />

        <input
          type="number"
          value={rounds}
          onChange={(e) => setRounds(e.target.value)}
          style={{
            padding: 10,
            width: 80,
            marginRight: 10,
            borderRadius: 6,
            border: "none",
          }}
        />

        <button
          onClick={startDebate}
          style={{
            padding: "10px 18px",
            background: "#2563eb",
            color: "white",
            border: "none",
            borderRadius: 6,
            cursor: "pointer",
          }}
        >
          Run Debate
        </button>
      </div>

      {loading && <p>⏳ Running debate...</p>}
      {data && <FlowView data={data} />}
    </div>
  );
}

export default App;
