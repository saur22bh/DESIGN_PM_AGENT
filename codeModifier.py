from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

import os 
import streamlit as st
os.environ["ANTHROPIC_API_KEY"] = st.secrets["ANTHROPIC_API_KEY"]

from langchain_anthropic import ChatAnthropic


llm = ChatAnthropic(model='claude-3-7-sonnet-20250219',
default_headers={
        "anthropic-beta": "max-tokens-3-5-sonnet-2024-07-15"
    },
    max_tokens=8192
                    )

# llm = ChatAnthropic(model='claude-3-5-sonnet-20241022',
# default_headers={
#         "anthropic-beta": "max-tokens-3-5-sonnet-2024-07-15"
#     },
#     max_tokens=8192
#                     )

prompt = '''
You are an AI that modifies HTML/React UI code based on instructions. Given a code snippet and modification instructions, return only the code, without explanations or additional text.

Input format:
1-Code : {Original}
2 -Modification instructions {instrubctions}

Note : The returned code should not just include the modifications but the full original input code with the requested changes applied
'''

CodeModifierPromptTemplate = PromptTemplate(template=prompt,input_variables=['Original','instrubctions'])
parser =StrOutputParser()

CodeModifierProcess = CodeModifierPromptTemplate|llm|parser 

Original = '''
import React, { useState } from 'react';
import { motion } from 'framer-motion';

export default function FitnessJourney() {
  const [showQuoteModal, setShowQuoteModal] = useState(false);
  const [selectedQuote, setSelectedQuote] = useState(null);

  const quotes = [
    {
      text: "The only bad workout is the one that didn't happen.",
      author: "Unknown",
      image: "https://images.unsplash.com/photo-1526506118085-60ce8714f8c5"
    },
    {
      text: "Your body can stand almost anything. It's your mind you have to convince.",
      author: "Unknown", 
      image: "https://images.unsplash.com/photo-1549576490-b0b4831ef60a"
    }
  ];

  const workouts = [
    {
      date: "2024-01-20",
      type: "Running",
      duration: "45 min",
      notes: "5k completed, feeling strong!",
      image: "https://images.unsplash.com/photo-1461896836934-ffe607ba8211"
    },
    {
      date: "2024-01-19",
      type: "Weight Training",
      duration: "60 min",
      notes: "New PR on deadlift!",
      image: "https://images.unsplash.com/photo-1583454110551-21f2fa2afe61"
    }
  ];

  return (
    <div className="min-h-screen bg-gray-900 text-gray-100 px-4 py-6">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="max-w-md mx-auto"
      >
        <h1 className="text-3xl font-bold text-emerald-400 mb-2">
          Fitness Journey
        </h1>
        <p className="text-gray-400 mb-8">
          Track progress. Stay motivated. Connect.
        </p>

        <section className="mb-8">
          <h2 className="text-xl font-semibold text-emerald-400 mb-4">
            Today's Motivation
          </h2>
          <div className="grid gap-4">
            {quotes.map((quote, i) => (
              <motion.div
                key={i}
                whileTap={{ scale: 0.98 }}
                onClick={() => {
                  setSelectedQuote(quote);
                  setShowQuoteModal(true);
                }}
                className="bg-gray-800 rounded-lg overflow-hidden cursor-pointer"
              >
                <img
                  src={quote.image}
                  alt="Motivation"
                  className="w-full h-48 object-cover"
                />
                <div className="p-4">
                  <p className="text-lg font-medium">{quote.text}</p>
                  <p className="text-sm text-gray-400 mt-2">- {quote.author}</p>
                </div>
              </motion.div>
            ))}
          </div>
        </section>

        <section className="mb-8">
          <h2 className="text-xl font-semibold text-emerald-400 mb-4">
            Workout Journal
          </h2>
          <div className="space-y-4">
            {workouts.map((workout, i) => (
              <motion.div
                key={i}
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                className="bg-gray-800 rounded-lg overflow-hidden"
              >
                <img
                  src={workout.image}
                  alt={workout.type}
                  className="w-full h-48 object-cover"
                />
                <div className="p-4">
                  <div className="flex justify-between items-center mb-2">
                    <h3 className="font-medium">{workout.type}</h3>
                    <span className="text-sm text-gray-400">{workout.date}</span>
                  </div>
                  <p className="text-sm text-gray-300">{workout.duration}</p>
                  <p className="text-gray-400 mt-2">{workout.notes}</p>
                </div>
              </motion.div>
            ))}
          </div>
        </section>

        <button className="w-full bg-emerald-500 hover:bg-emerald-600 text-white font-semibold py-3 px-6 rounded-lg transition duration-200">
          Find Workout Buddies
        </button>
      </motion.div>

      {showQuoteModal && (
        <div className="fixed inset-0 bg-black bg-opacity-75 flex items-center justify-center p-4">
          <motion.div
            initial={{ scale: 0.9, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            className="bg-gray-800 rounded-lg p-6 max-w-sm w-full"
          >
            <h3 className="text-xl font-semibold mb-4">{selectedQuote.text}</h3>
            <p className="text-gray-400">By {selectedQuote.author}</p>
            <button
              onClick={() => setShowQuoteModal(false)}
              className="mt-6 w-full bg-emerald-500 hover:bg-emerald-600 text-white font-semibold py-2 px-4 rounded transition duration-200"
            >
              Close
            </button>
          </motion.div>
        </div>
      )}
    </div>
  );
}

'''

# response = CodeModifierProcess.invoke({'Original':Original,'instrubctions':'Can you add 1-2 people profile in Find workout buddies section and a cta to book session with them'})
# print(response)
