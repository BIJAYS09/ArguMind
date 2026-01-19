import React, { useState } from "react";
import FlowView from "./FlowView";
import { runDebate } from "./api";

export default function App() {
  const [topic, setTopic] = useState("");
  const [rounds, setRounds] = useState(3);
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  const startDebate = async () => {
    setLoading(true);
    const result = await runDebate(topic, rounds);
    setData(result);
    setLoading(false);
  };

  return (
    <div style={{ background: "#020617", color: "white", minHeight: "100vh", padding: 20 }}>
      <h1 style={{ fontSize: 24 }}>🧩 DebateGraph AI</h1>

      <div style={{ margin: "20px 0" }}>
        <input
          placeholder="Enter debate topic"
          value={topic}
          onChange={(e) => setTopic(e.target.value)}
          style={{ padding: 8, width: 300, marginRight: 10 }}
        />

        <input
          type="number"
          value={rounds}
          onChange={(e) => setRounds(e.target.value)}
          style={{ padding: 8, width: 80, marginRight: 10 }}
        />

        <button
          onClick={startDebate}
          style={{
            padding: "8px 16px",
            background: "#2563eb",
            color: "white",
            border: "none",
          }}
        >
          Run Debate
        </button>
      </div>

      {loading && <p>Running debate...</p>}
      {data && <FlowView data={data} />}
    </div>
  );
}
