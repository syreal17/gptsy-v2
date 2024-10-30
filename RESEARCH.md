# Areas to investigate

- Creating "representative" samples of generations of a prompt.
- Finding the theoretical limit of all possible 1-word generations of a simple
  prompt.

1. **Defining and Exploring “Core Responses”**:
   - Observing patterns in high-frequency words, especially filler words, to identify the model’s “default” responses in vague prompts.
   - Investigating whether certain words (like “that,” “the,” “like”) appear more due to high-probability defaults and how that affects representativeness.

2. **Experimenting with Sampling Parameters**:
   - Exploring how parameters like temperature, top-p, and top-k affect diversity and creativity in responses. Adjusting these parameters might help capture a broader range of outputs beyond default words.
   - Determining an approach to assess representativeness by examining how these settings influence variability and convergence.

3. **Investigating Rare and Specific Words**:
   - Noting that words like “confident,” “threatened,” “fearful,” and “guilty” appeared in response to vague prompts.
   - Considering the impact of vague prompts on the emergence of more complex, introspective emotions rather than basic ones like “happy” or “sad.”
   - Testing whether more targeted prompts can elicit simpler emotions and clearer states.
   - Testing if changing the name of the person changes the emotions elicited.

4. **Alternative Prompts to Steer GPT’s Responses**:
   - Testing variations like “Lumere feels very…” to see if it encourages simpler emotional responses.
   - Additional prompt ideas:
     - “Lumere is feeling very…”
     - “Lumere feels, as if…” (for metaphoric or poetic responses)
     - “In her heart, Lumere feels…” (for potentially resonant or heartfelt emotions)
     - “When Lumere reflects, she feels…” (to encourage thoughtful, layered emotions)
     - “Lumere has been feeling…” (to draw out recurring or ongoing emotions)

5. **Theoretical Investigation into Sampling**:
   - Exploring the theoretical limits of sampling representativeness: Can we capture 99% of the model’s potential responses with a defined number of generations?
   - Discussing how combinatorial explosion and infinite generative potential affect representativeness in sampling, especially with high variability in response space.

6. **Experiment with Single-Word Responses for Direct Insights**:
   - Using prompts to generate only one-word responses to identify immediate associations or “core” terms for characters or emotions.

7. **Python Script Development**:
   - Implementing a script to count unique line occurrences for analyzing frequent responses in a large dataset.
   - Using command-line arguments to streamline script usability.

---
