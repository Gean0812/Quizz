const startButton = document.getElementById("start-btn")
const questioContainerElement = document.getElementById("question-container")
let shuffleQuestions ,currentQuestionIndex

const questionElement = document.getElementById("question")
const answerButtons = document.getElementById("answer-buttons")
const nextButton = document.getElementById("next-btn")

startButton.addEventListener('click',startGame)
nextButton.addEventListener('click', () =>{
    currentQuestionIndex++
    setNextQuestion()

})




function startGame(){
    console.log("Começou")
    startButton.classList.add("hide")
    shuffleQuestions = questions.sort(( ) => Math.random() -.4 )
    currentQuestionIndex = 0
    questioContainerElement.classList.remove("hide")
    setNextQuestion();

}

function setNextQuestion(){
    resetState()
    showQuestion(shuffleQuestions[currentQuestionIndex])

}

function showQuestion(question){
    questionElement.innerText = question.question
    question.answers.forEach(answer => {
        const button = document.createElement('button')
        button.innerText = answer.text
        button.classList.add('btn')
        if(answer.correct){
            button.dataset.correct = answer.correct
        }
        button.addEventListener('click',selectAnswer)
        answerButtons.appendChild(button)
        
    });

}

function selectAnswer(e){
    const selectedButton = e.target
    const correct = selectedButton.dataset.correct
    setStatusClass(document.body,correct)
    Array.from(answerButtons.children).forEach(button => {
        setStatusClass(button,button.dataset.correct)
    })
    if(shuffleQuestions.length > currentQuestionIndex + 1){
        nextButton.classList.remove('hide')
    } else{
        startButton.innerText = 'Restart'
        startButton.classList.remove('hide')
    }


}

function resetState(){
    nextButton.classList.add('hide')
    while(answerButtons.firstChild){
        answerButtons.removeChild(answerButtons.firstChild)
    }
}

function setStatusClass(element, correct){
    clearStatusClass(element)
    if(correct){
        element.classList.add('correct')
    } else{
        element.classList.add('wrong')
    }


}

function clearStatusClass(element){
    element.classList.remove('correct')
    element.classList.remove('wrong')
}


