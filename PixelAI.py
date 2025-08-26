import datetime
import os 
import time
import webbrowser
import pyttsx3 
import speech_recognition as sr 
import wikipedia 
from googlesearch import search
from urllib.parse import urljoin
from youtube_search import YoutubeSearch 
import pyjokes 
import pywhatkit
import inflect
import sys
from yaspin import yaspin
from termcolor import colored
from plyer import notification  
import yt_dlp  
from google import genai 

                             # INITIALIZING TEXT TO SPEECH ENGINE         


engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')

engine.setProperty('voices', voices[0].id)
                  
                             # TEXT TO SPEECH

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

                            # PRINTING TEXT WITH DELAY

def show(query,delay=0.01):
    for char in query:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

                            # GEMINI API

def gemini_api(query):
    try:
        client = genai.Client(api_key="AIzaSyDIuUg4_a-DN8Va61DdpZNnUpvphDB4Lek")
        if not query.strip():
            raise ValueError("Query is empty. Cannot process the request.")
        response = client.models.generate_content(model="gemini-2.0-flash", contents=query + " within 1-2 sentences")
        show(colored(response.text, "cyan"))
        speak(response.text)
    except ValueError as e:
        show(colored(f"Error: {str(e)}", "red"))
        speak("The query is empty. Please try again.")
    except Exception as e:
        show(colored(f"An error occurred: {str(e)}", "red"))
        speak("An error occurred while processing your request.")
    finally:
        input("Press Enter to continue...")
    
                              # NOTIFICATION

notification.notify(title="PIXEL",      
            message="PIXEL is starting on your local system",   
                        timeout=5)
                   
                             # STARTING INTERFACE
print(" ")
show(colored("██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████ \n ", "green"),delay=0.04)

with yaspin(text="Activating PIXEL 🤖",color="yellow") as spinner:
    time.sleep(3)
    spinner.text = colored("Please wait few seconds ⌛ ","yellow",on_color="on_black")
    time.sleep(5)
    spinner.text = (colored("PIXEL is ready to help you 🤖 \n",color="green",on_color="on_black",attrs=["bold"]))
    spinner.ok("✅")

notification.notify(title="PIXEL", message="PIXEL is activated 🤖" " "
"Say PIXEL to start conversation",timeout=5)

                             # WISHING  USER AS PER THE TIME
def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour >= 0 and hour < 12:
        show(colored("Good Morning ! \n","magenta"))
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        show(colored("Good Afternoon ! \n","magenta"))
        speak("Good Afternoon!")

    else:
        show(colored("Good Evening! \n","magenta"))
        speak("Good Evening!")

    show(colored("I am pixel, your personal A I. How can I help you ? \n","white",on_color="on_black"))
    speak("I am pixel, your personal AI. How can I help you?",)
    
                             # LISTENING FOR KEYWORD

def listen_for_keyword():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        show(colored("Say ' hiii pixel' to start... \n", "yellow" ,attrs=["bold"]))
        while True:
            audio = r.listen(source)
            try:
                keyword = r.recognize_google(audio, language='en-in')
                if 'pixel' in keyword or  " hello pixel " in keyword or "hey pixel" in keyword or "hello" in keyword or ' hi pixel' in keyword:
                    speak("Yes, Sir.")
                    show(colored("Yes, Sir. \n","cyan"))
                    return True
            except Exception as e:
                continue

                                # TAKING COMMAND FROM USER

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        show(colored("Listening...... \n", "green"))
        r.pause_threshold = 1.00
        try:
            audio = r.listen(source, timeout=3, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            show(colored("No speech detected. Please try again.", "red"))
            speak("No speech detected. Please try again.")
            return "None"
        except Exception as e:
            show(colored(f"An error occurred: {str(e)}", "red"))
            speak("An error occurred while listening.")
            return "None"

    try:
        show(colored("Recognising.... \n", "blue"))
        query = r.recognize_google(audio, language='en-in')
        if not query.strip():
            show(colored("Could not understand. Please speak clearly.", "red"))
            speak("Could not understand. Please speak clearly.")
            return "None"
        show(colored(f"  User said: {query}  \n", "yellow", attrs=["bold"]))
    except sr.UnknownValueError:
        show(colored("Could not understand audio. Please speak clearly.", "red"))
        speak("Could not understand audio. Please speak clearly.")
        return "None"
    except sr.RequestError as e:
        show(colored(f"Could not request results; {e}", "red"))
        speak("Sorry, there was an error with the speech recognition service.")
        return "None"
    except Exception as e:
        show(colored(f"An error occurred: {str(e)}", "red"))
        speak("An error occurred while recognizing speech.")
        return "None"
    return query

def tell_joke():
    joke = pyjokes.get_joke()
    show(colored(joke, "cyan"))
    speak(joke)
           
             # DOWNLOADING YOUTUBE VIDEOS

def download(query):
    try:
        results = YoutubeSearch(query).to_dict()  
        if results:
            first_result = results[0]
            url_suffix = first_result.get('url_suffix')  # .get() for avoid KeyError
            if url_suffix:
                base_url = "https://www.youtube.com"  
                video_url = urljoin(base_url, url_suffix)  
                title = first_result.get('title', 'Unknown Title')  # Get video title
                print(colored(f"Downloading: {title}", "cyan" ,attrs= ["bold"]))  # Print the name of the song
                speak(f"Downloading {title}")

                ydl_opts = {'format': 'bestvideo+bestaudio/best', 'outtmpl': '%(title)s.%(ext)s'}
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([video_url])

                print(colored(f"Download completed: {title}", "green", attrs= ["bold"]))
                speak(f"Download completed: {title}")
            else:
                print("No URL suffix found in search results.")
        else:
            print("No results found for your query.")
    except Exception as e:  # Catch errors during search or download
        show(colored(f"An error occurred during download: {str(e)}", "red"))
        speak("An error occurred during the download process.")
    finally:
        input("Press Enter to continue...")

def word():
    p = inflect.engine()
    num = query
    words = p.number_to_words(num)
    show(colored(words, "cyan"))
    speak(words)
    return

def handle_query(query):
    try:
        
                              # COMMANDS FOR SEARCHING ON WIKIPEDIA
                              
        if 'wikipedia' in query or 'search on wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", " ")
            notification.notify(title="PIXEL", message="Access Wikipedia", timeout=2, app_name="PIXEL")
            try:
                results = wikipedia.summary(query, sentences=5)
                show(colored("According to Wikipedia", "cyan"))
                print(" ")
                speak("According to Wikipedia")
                show(colored(results, "cyan"))
                speak(results)
                print(" ")
            except wikipedia.exceptions.DisambiguationError as e:
                show(colored("The query is ambiguous. Please be more specific.", "red"))
                speak("The query is ambiguous. Please be more specific.")
            except wikipedia.exceptions.PageError as e:
                show(colored("No matching page found on Wikipedia.", "red"))
                speak("No matching page found on Wikipedia.")
            except Exception as e:
                show(colored(f"An error occurred: {str(e)}", "red"))
                speak("An error occurred while searching Wikipedia.")
            input("Press Enter to continue...")

        elif "what is my previous question "in query or"what is my previous search" in query or "previous search" in query or "what is my previous command" in query:
            gemini_api()

        elif 'who made you' in query or 'who created you' in query or 'who is your creator' in query or 'who developed you' in query or 'who is your developer' in query or 'devloped by' in query:
            show(colored("I have been created by RASMI RANJAN NAYAK!","cyan"))
            speak("I have been created by RASMI RANJAN NAYAK!")
            
                                # WEATHER ASSISTANT    
        
        elif 'weather' in query or 'what is the weather at ' in query or 'what is the weather in ' in query:
            notification.notify(title="PIXEL", message=" Access Accuweather in chrome ",timeout=2)
            show(colored("searching on accuweather...... \n ","cyan"))
            speak("searching on accuweather......")
            query = query.replace("weather", " ")
            query = query.replace("what is weather in ", " ")
            results = search("https://www.accuweather.com/" + query, num_results=1)
            for result in results:
                webbrowser.open_new(result)
            input("Press Enter to continue...")

        elif  'play on youtube' in query or 'play'  in query or 'youtube' in query:
            query = query.replace("play on youtube", " ").strip()
            query = query.replace("play", " ").strip()
            if not query:
                show(colored("No query provided for YouTube search.", "red"))
                speak("No query provided for YouTube search.")
            else:
                notification.notify(title="PIXEL", message="Accessing YouTube", timeout=2)
                try:
                    pywhatkit.playonyt(query)
                    show(colored("Playing on YouTube: " + query, "cyan"))
                    speak("Playing on YouTube: " + query)
                except Exception as e:
                    show(colored(f"An error occurred: {str(e)}", "red"))
                    speak("An error occurred while trying to play on YouTube.")
            input("Press Enter to continue...")

                                # DOWNLOADING YOUTUBE VIDEO

        elif 'download ' in query:
                query = query.replace("download", " ")
                download(query)

                                # OPENING WEBSITES

        elif 'open youtube' in query:
            webbrowser.open_new_tab("https://www.youtube.com")
            notification.notify(title="PIXEL", message="  Access Youtube ",timeout=2)
            speak("youtube is open now")
            input("Press Enter to continue...")

        elif 'open amazon' in query:
            webbrowser.open_new_tab("https://www.amazon.in")
            notification.notify(title="PIXEL", message="  Access Amazon ",timeout=2)    
            speak("Amazon is open now")
            input("Press Enter to continue...")

        elif 'open flipkart' in query:
            webbrowser.open_new_tab("https://www.flipkart.com")
            notification.notify(title="PIXEL", message="  Access Flipkart ",timeout=2)
            speak("flipkart is open now")
            input("Press Enter to continue...")

        elif 'open google' in query:
            webbrowser.open_new_tab("https://www.google.com")
            notification.notify(title="PIXEL", message="  Access Google ",timeout=2)
            speak("Google is open now")
            input("Press Enter to continue...")

        elif 'open gmail' in query:
            webbrowser.open_new_tab("https://accounts.google.com/login")
            notification.notify(title="PIXEL", message="  Access Gmail ",timeout=2)
            speak("Google Mail is open now")
            input("Press Enter to continue...")

                                # SYSTEM COMMANDS

        elif "what's time now" in query or 'what is time now' in query or 'what is the time now' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            show(colored(f"Sir, The Time is {strTime}","cyan"))
            speak(f"Sir, The Time is {strTime}")
            
        elif 'what can you do' in query or 'what can you do for me' in query or 'who are you' in query or 'what is your purpose' in query or 'what is your job' in query or 'what is your work' in query or 'what is your role' in query:
            show(colored("I am PIXEL , a personal artificial intelligence, if you prefer. I was created by TECH ARMY FROM MIPS to help you in many different ways,  You can also talk to me about something serious or just have a fun conversation. I’m here for you.","cyan"))
            speak("I am PIXEL, a personal artificial intelligence, if you prefer. I was created by TECH ARMY FROM MIPS to help you in many different ways,  You can also talk to me about something serious or just have a fun conversation. I’m here for you.")
            
        elif 'locate me' in query:
            query = query.replace("locate", "")
            query = query.replace("where is", "")
            location = query
            speak("Sir here is")
            notification.notify(title="PIXEL", message="  Access Google Maps ",timeout=2)
            show(colored("searching on google maps......","cyan"))
            speak("location")
            webbrowser.open(
                "https://www.google.com/maps/place/" + location + "")
            input("Press Enter to continue...")
        
        elif 'what is your name' in query or 'what is your name' in query:
            show(colored("my name is pixel","cyan"))
            speak("my name is pixel")
            
        elif ' what is your version ' in query or 'version' in query or 'can you tell me what is your version number' in query:
            show(colored("my version number is 1.0 , i created by tech army from mips , i am here to help you","cyan"))
            speak(" my version number 1.0 , i created by tech army from mips , i am here to help you")
            
            

        elif 'search on google' in query or 'who is' in query or 'what is' in query:
            query = query.replace("search on google", " ")
            query = query.replace("who is", " " + "search on wikipedia")
            query = query.replace("what is", " ")
            results = search(query, num_results=1)
            show(colored("Here is what I found on google","cyan"))
            speak("Here is what I found on google")
            for result in results:
                webbrowser.open_new_tab(result)
            input("Press Enter to continue...")

        elif "in word" in query or "words" in query:
            word()        
                                          # FUN ASSISTANT

        elif 'tell me a joke' in query or 'joke' in query:
            tell_joke()
            input("Press Enter to continue...")
            
                                          # GREETINGS

        elif 'good morning' in query:
            show(colored("A warm good morning","cyan"))
            speak("A warm good morning")
            show(colored("How are you Sir","cyan"))
            speak("How are you Sir")
        elif 'good afternoon' in query:
            show(colored("Yes, you too, thanks","cyan"))
            speak("Yes, you too, thanks")
            show( colored("How are you Sir...hope you are doing well","cyan"))
            speak("How are you Sir...")
        elif 'good evening' in query:
            show(colored("Yes, you too, thanks","cyan"))    
            speak("Yes, you too, thanks")
            show( colored("How are you Sir...hope you are doing well","cyan"))  
            speak("How are you Sir...hope you are doing well")
        elif 'good night' in query:
            show(colored("very Good Night Sir....sweet dreams","cyan"))    
            speak("very Good Night Sir....sweet dreams")
            
        elif 'who are you' in query:
            show(colored("I am your pixel created by tech army from mips !","cyan"))    
            speak("I am your pixel created by tech army from mips !")
            
        elif 'hi PIXEL' in query or 'hello PIXEL' in query or 'hai PIXEL' in query or 'hello' in query:
            show(colored("Hey There Whats up","cyan"))
            speak("Hey There Whats up")
            
        elif 'how are you'in query or 'how r u'in query:
            show(colored("I am fine, Sir","cyan"))
            speak("I am fine, Sir")
            show(colored("How can I help you","cyan"))
            speak("How can I help you")
        elif'bye pixel' in query or 'goodbye pixel' in query or 'good bye' in query or 'exit' in query or 'quit' in query:
            show(colored("Goodbye Sir","cyan"))
            speak("Goodbye Sir")
            show(colored("I am always here to help you","cyan"))
            speak("I am always here to help you")
            exit()
            
        elif 'i am fine'in query or'fine' in query or 'i am good' in query or 'good' in query :
            show(colored("It's good to know that your fine","cyan"))
            speak("It's good to know that your fine")
            show(colored("How can I help you","cyan"))
            speak("How can I help you")

        elif 'what about you' in query or 'how about you' in query:
            show(colored("i am also good sir","cyan"))
            speak("i am also good sir")

        elif'sure' in query or 'yes' in query or 'ok' in query:
            show(colored("How can I help you","cyan"))
            speak("please tell me.....")

                                          # HEALTH ASSISTANT
                                          
        elif 'i am suffering from fever' in query or 'fever' in query or 'suffering from fever' in query:
            show(colored("You can take paracetamol or asprin","cyan"))
            speak("You can take paracetamol or asprin")
  
        elif 'i am suffering from headache' in query or 'headache' in query or 'suffering from headache' in query:
            show(colored("You can take disprin","cyan"))
            speak("You can take disprin") 
   
        elif 'i am suffering from cough and cold' in query or 'cough and cold' in query or 'suffering from cough and cold' in query:
            show(colored("You can take cough syrup","cyan"))
            speak("You can take amoxicillin")
        
        elif 'i am suffering from diabetes' in query or 'diabetes' in query or 'suffering from diabetes' in query:
            show(colored("You can take insulin lispro","cyan"))
            speak("You can take insulin lispro")

        elif 'i am suffering from stomach ache' in query or 'stomach ache' in query or 'suffering from stomach ache' in query:
            show(colored("You can take antacids","cyan"))
            speak("You can take panadol")

        elif 'i am suffering from skin allergy' in query or 'allergy' in query or 'suffering from allergy' in query:
            show(colored("You can take antihistamines","cyan"))
            speak("You can take allegra")

        elif 'i am suffering from vomiting' in query or 'vomiting' in query or 'suffering from vomiting' in query:
            show(colored("You can take ondansetron","cyan"))
            speak("You can take dolasetron")

        elif 'i am suffering from depression' in query or 'depression' in query or 'suffering from depression' in query:
            show(colored("You can take sertraline","cyan"))
            speak("You can take lexapro")

        elif 'i am suffering from chickenpox' in query or 'chickenpox' in query or 'suffering from chickenpox' in query:
            show(colored("You can take a cool bath with added baking soda and you can also take benadryl","cyan"))
            speak("You can take a cool bath with added baking soda and you can also take benadryl")

        elif 'i am suffering from arthritis' in query or 'arthritis' in query or 'suffering from arthritis' in query:
            show(colored("You can take immunosupressive drug and analgesic","cyan"))
            speak("You can take immunosupressive drug and analgesic")

        elif 'i am suffering from asthma' in query or 'asthma' in query or 'suffering from asthma' in query:
            show(colored("You have to quit smoking and can take anti inflammatory drug","cyan"))
            speak("You have to quit smoking and can take anti inflammatory drug")

        elif 'i am suffering from bipolar disorder' in query or 'bipolar disorder' in query or 'suffering from bipolar disorder' in query:
            show(colored("You can take antipsychotic drugs","cyan"))
            speak("You can take antipsychotic drugs")

        elif 'i am suffering from chest pain' in query or 'chest pain' in query or 'suffering from chest pain' in query:
            show(colored("You can take nitroglycerine drugs","cyan"))
            speak("You can take nitroglycerine drugs")

        elif 'i am suffering from conjunctvitis' in query or 'conjunctvitis' in query or 'suffering from conjunctvitis' in query:
            show(colored("You can maintain hygeine and self heal with cold compress","cyan"))
            speak("You can maintain hygeine and self heal with cold compress")

        elif 'i am suffering from constipation' in query or 'constipation' in query or 'suffering from constipation' in query:
            show(colored("You can take stool softener and fibre supplement","cyan"))
            speak("You can take stool softener and fibre supplement")

        elif 'i am suffering from dehydration' in query or 'dehydration' in query or 'suffering from dehydration' in query:
            show(colored("You can take oral rehydration solution","cyan"))
            speak("You can take oral rehydration solution")

        elif 'i am suffering from food poison' in query or 'food poison' in query or 'suffering form food poison' in query:
            show(colored("ensure adequate hydration and take rehydration solution","cyan"))
            speak("ensure adequate hydration and take rehydration solution")

        elif 'i am suffering from flu' in query or 'flu' in query or 'suffering from flu' in query:
            show(colored("You can take bed rest and antiviral drug","cyan"))
            speak("You can take bed rest and antiviral drug ")

        elif 'i am suffering from indigestion' in query or 'indigestion' in query or 'suffering from indigestion' in query:
            show(colored("You can take antacids and oral suspension medicines","cyan"))
            speak("You can take antacids and oral suspension medicines")

        elif 'i am suffering from insomnia' in query or 'insomnia' in query or 'suffering from insomnia' in query:
            show(colored("You can take sedatives and anti depressants","cyan"))
            speak("You can take sedatives and anti depressants")

        elif 'i am suffering from malaria' in query or 'malaria' in query or 'suffering from malaria' in query:
            show(colored("You can take anti parasites and antibiotics","cyan"))
            speak("You can take anti parasites and antibiotics")

        elif 'i am suffering from malnutrition' in query or 'malnutrition' in query or 'suffering from malnutrition' in query:
            show(colored("You can high protein diet and nutiritive suppliments","cyan"))
            speak("You can high protein diet and nutiritive suppliments")

        elif 'i am suffering from obesity' in query or 'obesity' in query or 'suffering from obesity' in query:
            show(colored("You  have to do physical exercise and take low fat diet","cyan"))
            speak("You  have to do physical exercise and take low fat diet")

        elif 'i am suffering from panic disorder' in query or 'panic disorder' in query or 'suffering from panic disorder' in query:
            show(colored("You can take anti anxiety drugs","cyan")) 
            speak("You can take anti depressants")

        elif 'i am suffering from scabies' in query or 'scabies' in query or 'suffering from scabies' in query:
            show(colored("You can take anti parasite drugs","cyan"))
            speak("You can take anti parasite drugs")

        elif 'i am suffering from hiv' in query or 'hiv' in query or 'suffering from hiv' in query:
            show(colored("there is no medicine for hiv your meeting is fixed with god","cyan"))
            speak("there is no medicine for hiv your meeting is fixed with god")

        elif 'i am suffering from aids' in query or 'aids' in query or 'suffering from aids' in query:
            show(colored("there is no medicine for aids your meeting is fixed with god","cyan"))
            speak("there is no medicine for aids your meeting is fixed with god")

        elif 'i am suffering from cancer' in query or 'cancer' in query or 'suffering from cancer' in query:
            show("cancer medicine is not invented till yet you have to do operation")
            speak("cancer medicine is not invented till yet you have to do operation")

        elif 'i am suffering from Jaundice' in query or 'Jaundice' in query or 'suffering from Jaundice' in query:
            show(colored("You can take oral rehydration therapy and in critical case consult doctor","cyan"))
            speak("You can take oral rehydration therapy and in critical case consult doctor")

        elif 'i am suffering from acne' in query or 'acne' in query or 'suffering from acne' in query:
            show(colored("You can apply aloe vera and take vitamin a derivatives","cyan"))
            speak("You can apply aloe vera and take vitamin a derivatives")
             
        elif 'thank you' in query or 'thank' in query:
            show(colored("You are welcome","cyan"))
            speak("I am always here to help you")
            show(colored("I am always here to help you","cyan"))
            speak("I am always here to help you")
            input("Press Enter to continue...")
                   
        elif ' ' in query:
            if not query.strip():
                show(colored("No valid query provided.", "red"))
                speak("No valid query provided.")
            else:
                show(colored("Wait for a moment....", "green"))
                speak("Wait for a moment....")
                gemini_api(query)
        else:
            show(colored("Sorry, I didn't understand that. Please try again.", "red"))
            speak("Sorry, I didn't understand that. Please try again.")
            
    except Exception as e:
        show(colored(f"An error occurred while handling the query: {str(e)}", "red"))
        speak("An error occurred while handling your query. Please try again.")

wishMe()
listen_for_keyword()

while True:
    try:
        query = takeCommand().lower()
        if query == "none" or not query.strip():  # Skip invalid queries
            continue
        handle_query(query)
    except Exception as e:
        show(colored(f"An unexpected error occurred: {str(e)}", "red"))
        speak("An unexpected error occurred. Please try again.")