;
;The provided clojure program can be excuted using https://replit.com/
;steps to execute the code:
;1. It would be required to create an account first to use the online IDE
;2. When the 'Start building with a template' appears please click in Browse templates at the bottom right of the dialog box
;3. Search and select closure and then provide a title to the workspace adn then click on create repl
;4. Once the environment is setup copy and paste the program and click on the Run button on the top-middle of the screen. 
;5. The out should appear on the left side console
;
;The below clojure program uses a main function as adriver code
;It fisrt extracts the stopwords from a URL and then extracts and preprosses the words from the book URL
; once the preprocessing is completed the tokenize-and-count function removes the stopwords and assigns frequency for each word followed by sorting the words based on frequency and finaly returns the top ten
;the top ten words allong with their count are then printed
;


(ns main
(:require [clojure.string :as str]
[clojure.java.io :as io]))

(def stop-words-url "https://raw.githubusercontent.com/vedantMahangade/DAA-CSCI-6212-Project-Code/main/stopwords.txt")

(defn get-stop-words [url]
(let [input-stream (io/input-stream url)
reader (io/reader input-stream)]
(with-open [rdr reader]
(->> rdr
slurp
(clojure.string/split-lines)))))

(defn get-moby-dick-text [url]
(let [input-stream (io/input-stream url)
reader (io/reader input-stream)]
(with-open [rdr reader]
(->> rdr
slurp
(clojure.string/split-lines)))))

(defn clean-mdb-text [text]
(let [lower-case (str/lower-case text)
remove-numbers (str/replace lower-case #"[^a-z ]" "")
split-text (str/split remove-numbers #"\s+")]
split-text))

(defn tokenize-and-count [text stop-words]
(->> text
(remove (set stop-words))
frequencies
(sort-by val >)
(take 10)))

(defn main []
(let [stop-words (get-stop-words stop-words-url)
moby-dick-url "https://www.gutenberg.org/cache/epub/2489/pg2489.txt"
moby-dick-text (get-moby-dick-text moby-dick-url)
clean-text (clean-mdb-text moby-dick-text)
common-words (tokenize-and-count clean-text stop-words)]
(println "10 most common words:")
(doseq [[word count] common-words]
(println (str word ": " count)))))

(main)