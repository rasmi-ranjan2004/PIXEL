# Pixel AI: Voice-Activated Personal Assistant


Pixel AI is a Python-based voice-activated personal assistant that responds to voice commands, performs web searches, plays YouTube videos, provides health advice, tells jokes, and much more — all through natural voice interaction.


✨ Features
🎤 Voice-Activated: Wake word detection ("Pixel", "Hello Pixel")

🌐 Web Integration: Google search, Wikipedia queries, website navigation

📺 YouTube Control: Play and download videos via voice commands

🏥 Health Assistant: Basic medical advice for common symptoms (with disclaimer)

😄 Entertainment: Tell jokes, convert numbers to words, time-based greetings

🤖 AI-Powered: Gemini AI integration for intelligent responses

💬 Text-to-Speech: Audible responses using pyttsx3

🔔 Notifications: Desktop alerts for system events

🎨 Interactive CLI: Colored output with typing animation effects

🚀 Quick Start
Prerequisites
Python 3.10 or higher

Microphone

Internet connection (for most features)

Installation
Clone the repository:

bash
git clone https://github.com/your-username/pixel-ai.git
cd pixel-ai
Install dependencies:

bash
pip install -r requirements.txt
Get your Gemini API key from Google AI Studio and replace the placeholder in PixelAI.py:

python
client = genai.Client(api_key="YOUR_API_KEY_HERE")
Run the assistant:

bash
python PixelAI.py
🗣️ Usage
Activation
Say one of the wake phrases:

"Hello Pixel"

"Hey Pixel"

"Hi Pixel"

Available Commands
Command Type	Examples
Web Search	"Search Python on Google", "Who is Albert Einstein"
Wikipedia	"Search artificial intelligence on Wikipedia"
YouTube	"Play shape of you on YouTube", "Download Python tutorial"
Health	"I am suffering from fever", "I have a headache"
Utilities	"What's the time", "Tell me a joke", "Open Google"
Conversation	"How are you", "What can you do", "Good morning"
🛠️ Technology Stack
Python 3.10+ - Core programming language

SpeechRecognition - Voice input processing

pyttsx3 - Text-to-speech conversion

Google Gemini API - AI-powered responses

Wikipedia API - Information retrieval

yt-dlp - YouTube video downloading

pywhatkit - YouTube video playback

plyer - Desktop notifications

termcolor - Colored terminal output

📁 Project Structure
text
pixel-ai/
├── PixelAI.py          # Main application
├── requirements.txt    # Dependencies
├── README.md          # This file
└── assets/            # Screenshots and demo files
🔧 Customization
You can extend Pixel AI by:

Adding new commands: Modify the handle_query() function

Integrating new APIs: Add API wrapper functions

Customizing responses: Edit the response strings throughout the code

Changing voice: Modify pyttsx3 voice properties

⚠️ Disclaimer
Important: The health advice provided by Pixel AI is generic and for informational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of qualified healthcare providers with any questions about medical conditions.

🤝 Contributing
We welcome contributions! Please feel free to submit issues, feature requests, or pull requests.

Fork the project

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

👥 Developers
Abhishek Nanda

Ananta Swain

Anup Kumar Prusty

Asish Panigrahi

Jinendra Halwa

Rasmi Ranjan Nayak

Under the guidance of Prof. Ramanuja Nayak

🙏 Acknowledgments
Google for the Gemini API

Python community for excellent libraries

Berhampur University for academic support

MITS Institute of Professional Studies for resources

📞 Support
For questions or support, please contact:

Email: [project team email]

Issues: GitHub Issues

<div align="center">
"Technology is best when it brings people together." – Matt Mullenweg

</div>
