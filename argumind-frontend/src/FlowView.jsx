import React from "react";
import ReactFlow, { Background, Controls } from "reactflow";
import "reactflow/dist/style.css";

export default function FlowView({ data }) {
  if (!data) return null;

  const nodes = [
    {
      id: "input",
      position: { x: 300, y: 0 },
      data: { label: `Topic: ${data.topic}` },
      style: { background: "#1f2937", color: "white", padding: 10 },
    },
    {
      id: "pro",
      position: { x: 0, y: 150 },
      data: { label: `🟢 Pro:\n${data.pro_history.join("\n\n")}` },
      style: { background: "#065f46", color: "white", width: 250 },
    },
    {
      id: "contra",
      position: { x: 600, y: 150 },
      data: { label: `🔴 Contra:\n${data.contra_history.join("\n\n")}` },
      style: { background: "#7f1d1d", color: "white", width: 250 },
    },
    {
      id: "judge",
      position: { x: 150, y: 350 },
      data: { label: `⚖ Judge:\n${data.verdict}` },
      style: { background: "#1e40af", color: "white", width: 300 },
    },
    {
      id: "critic",
      position: { x: 150, y: 550 },
      data: { label: `🧪 Critic:\n${data.critic_review}` },
      style: { background: "#312e81", color: "white", width: 300 },
    },
  ];

  const edges = [
    { id: "e1", source: "input", target: "pro", animated: true },
    { id: "e2", source: "input", target: "contra", animated: true },
    { id: "e3", source: "pro", target: "judge", animated: true },
    { id: "e4", source: "contra", target: "judge", animated: true },
    { id: "e5", source: "judge", target: "critic", animated: true },
  ];

  return (
    <div style={{ height: "80vh" }}>
      <ReactFlow nodes={nodes} edges={edges} fitView>
        <Background />
        <Controls />
      </ReactFlow>
    </div>
  );
}
