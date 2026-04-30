type Vote = boolean;

interface Agent {
  id: number;
  faction: number;
  stake: number;
  voteCache?: Vote;
}

interface PredictionOutput {
  question: string;
  totalAgents: number;
  yesWeight: number;
  noWeight: number;
  confidenceScore: number;
  factionBreakdown: Record<number, { yes: number; no: number; weight: number }>;
  rawVotes: Record<number, Vote>;
}

// ------------------------------
// FACTION BIAS SYSTEM
// ------------------------------

function getFactionBias(faction: number): number {
  switch (faction) {
    case 1: return 0.25; // bullish
    case 2: return -0.25; // bearish
    case 3: return 0; // neutral
    case 4: return -0.1; // risk-averse
    case 5: return 0.3; // hype/speculative
    case 6: return -0.2; // contrarian
    default: return 0;
  }
}

// ------------------------------
// AGENT VOTE LOGIC
// ------------------------------

function vote(agent: Agent, question: string): Vote {
  if (agent.voteCache !== undefined) return agent.voteCache;

  const bias = getFactionBias(agent.faction);

  const randomness = (Math.random() - 0.5); // -0.5 to +0.5
  const score = bias + randomness;

  const result = score > 0;

  agent.voteCache = result;
  return result;
}

// ------------------------------
// MAIN ENGINE
// ------------------------------

export function runPrediction(question: string): PredictionOutput {
  console.log("ENGINE IS RUNNING");

  const agents: Agent[] = [];
  const factionBreakdown: Record<number, { yes: number; no: number; weight: number }> = {};
  const rawVotes: Record<number, Vote> = {};

  let yesWeight = 0;
  let noWeight = 0;

  // init factions
  for (let i = 1; i <= 6; i++) {
    factionBreakdown[i] = { yes: 0, no: 0, weight: 0 };
  }

  // create 1020 agents
  for (let i = 0; i < 1020; i++) {
    agents.push({
      id: i,
      faction: (i % 6) + 1,
      stake: Math.floor(Math.random() * 100) + 1,
    });
  }

  // voting phase (IMPORTANT: only once per agent)
  for (const agent of agents) {
    const result = vote(agent, question);
    rawVotes[agent.id] = result;

    const weight = agent.stake;

    if (result) {
      yesWeight += weight;
      factionBreakdown[agent.faction].yes++;
    } else {
      noWeight += weight;
      factionBreakdown[agent.faction].no++;
    }

    factionBreakdown[agent.faction].weight += weight;
  }

  const confidenceScore = calculateConfidence(yesWeight, noWeight);

  return {
    question,
    totalAgents: 1020,
    yesWeight,
    noWeight,
    confidenceScore,
    factionBreakdown,
    rawVotes,
  };
}

// ------------------------------
// CONFIDENCE ENGINE
// ------------------------------

function calculateConfidence(yes: number, no: number): number {
  const total = yes + no;
  if (total === 0) return 0;

  return Math.round((Math.abs(yes - no) / total) * 100);
}