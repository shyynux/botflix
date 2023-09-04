<p align="center">
  <picture>
    <img alt="Botflix Chatbot" src="assets/logo-bot.png" width="352" height="59" style="max-width: 100%;">
  </picture>
  <br/>
  <br/>
</p>

<h3 align="center">
    <p>✨ Botflix is a chatbot built using Textbase. ✨</p>
</h3>

## What is botflix? 
- Botflix internally uses OpenAI's models(GPT - 3.5), just like ChatGPT, with the help of prompt engineering, it is able to identify as botflix.
- It can recommend TV shows, movies, anime etc accurately because of the additional context provided by the Netflix API.
- Apart from the shows, it also provides direct links to the shows, which will help the user to directly browse Netflix via botflix.
- Botflix stores last conversations and curate newer responses based on them.
- It stores only relevant information like the title, cast, number of episodes etc., which the user can ask in follow up queries.
- Since it uses GPT-3.5, there will never be an empty, repetitive or a placeholder response which are not engaging.

### Technologies used
- API used : Used the unofficial [Netflix](https://rapidapi.com/Glavier/api/netflix54) API to search accurate and recent results.
- Backend: Python
- Frontend and Bot implementation: Textbase was used, [Textbase](https://docs.textbase.ai) is a tool which makes making chatbots easy.

Try out the bot [here]{link}

### How to use this bot locally?
Since textbase is used, we need to follow these steps - 
1. Clone this repo, for details see [textbase-installation]([link](https://docs.textbase.ai/usage))
2. Add OpenAI and RapidAPI key in .env file.(Both of these are free to use for some amount of requests)
3. Follow the steps to here.

### Future additions
- [ ] Custom prompts to make the responses better.
- [ ] Integrating image and video embedding in the bot.
- [ ] Support for voice input.

### `Enjoy!!!
