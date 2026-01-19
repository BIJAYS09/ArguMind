import axios from "axios";

export const runDebate = async (topic, rounds) => {
  const res = await axios.post("http://localhost:8000/run", {
    topic,
    rounds,
  });
  return res.data;
};
