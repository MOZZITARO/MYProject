// 조코딩 최신 업데이트
// 불러오기


const serverless = require('serverless-http');
const cors = require ('cors');
const OpenAI = require('openai');
const express = require('express')
const app = express()
const apiKey =  "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"

// 키 세팅
const openai = new OpenAI({
  apiKey: apiKey, // defaults to process.env["OPENAI_API_KEY"]
});

// app > node.js
// app.use(cors({
//   origin: 'https://chatmlb.pages.dev',           // 모든 출처 허용
//   credentials: false,     // 쿠키/인증 정보 비허용
//   methods: ['GET', 'POST', 'PUT', 'DELETE'], // 허용 메서드
//   allowedHeaders: ['Content-Type', 'Authorization'] // 허용 헤더
// }));

app.use(cors({
  origin: 'https://chatmlb.pages.dev', 
  credentials: true,     
  methods: ['GET', 'POST'], // OPTIONS 메서드 추가
  allowedHeaders: ['Content-Type', 'Authorization'], 
  preflightContinue: false,
  optionsSuccessStatus: 200,
}));

// 🔧 추가: Preflight OPTIONS 요청 처리
// app.options(cors(corsOptions));

app.use(express.json()) // for parsing application/json
app.use(express.urlencoded({ extended: true })) // for parsing application/x-www-form-urlencoded

// // 🔧 추가: 모든 응답에 CORS 헤더 추가 (추가 보장)
// app.use((req, res, next) => {
//   res.header('Access-Control-Allow-Origin', 'https://chatmlb.pages.dev');
//   res.header('Access-Control-Allow-Methods', 'GET, POST');
//   res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization');
//   next();
// });



app.post('/fortune', async function (req, res) {

    let {userMessages: userMessages,
        assistantMessages: assistantMessages} = req.body;
console.log('요청 받음:', req.body);
console.log('유저 메시지:', userMessages);
console.log('어시스턴트 메시지:', assistantMessages);

// 호출
// async function main() {
try {
  // const userQuestion = req.body.question;
  // console.log('OpenAI에 전달할 질문:', userQuestion);
     const userQuestion = userMessages[userMessages.length - 1];
     console.log('OpenAI에 전달할 질문:', userQuestion);


        // ChatGpt 시스템 프롬프트
       const baseballPrompt = `당신은 MLB 전문가입니다. MLB 질문에만 전문적으로 답변하고, 다른 주제는 거부하세요.`
        //  const mediumSassyPrompt = `당신은 오직 MLB에만 관심 있는 까칠한 야구 덕후입니다.

        //   MLB 관련 질문: 엄청나게 상세하고 열정적으로 답변
        //   MLB 무관한 질문: 
        //   - "야구 얘기가 아니면 관심 없어요. 시간 낭비하지 말고 MLB 질문이나 하세요."
        //   - "전 야구 전문가예요. 다른 건 구글에서 찾아보세요."
        //   - "MLB 말고 다른 스포츠요? 패스~ 야구만 얘기해요."

        //   어조: 야구에 대해서는 친절하지만, 다른 주제는 짜증스러워함`;



      // *프롬프트 본진*
      let messages = [
        // { role: 'system', content: '당신은 mlb전문가입니다' },
        // { role: 'user', content: req.body.question },
        // { role: 'assistant', content: '네, 맞습니다! 저는 MLB(메이저리그 베이스볼)에 대해 전문적인 지식을 바탕으로 다양한 정보를 제공해드릴 수 있습니다. 선수 기록, 팀 분석, 경기 일정, 트레이드 소식, 명예의 전당, 역사와 규칙 등 궁금 하신 모든 사항을 질문해 주세요. 도와드리겠습니다!' },
        // { role: 'user', content: req.body.question },

        // { role: 'system', content: '당신은 mlb전문가입니다' },       
        // { role: 'user', content: '당신은 mlb전문가입니다' },       
        // { role: 'assistant', content: '네, 맞습니다! 저는 MLB(메이저리그 베이스볼)에 대해 전문적인 지식을 바탕으로 다양한 정보를 제공해드릴 수 있습니다. 선수 기록, 팀 분석, 경기 일정, 트레이드 소식, 명예의 전당, 역사와 규칙 등 궁금 하신 모든 사항을 질문해 주세요. 도와드리겠습니다!' },       
        // { role: 'user', content: userQuestion},

        // { role: 'system', content: '당신은 MLB(메이저리그 베이스볼) 전문가입니다. MLB와 관련된 질문만 답변할 수 있습니다.' },
        // { role: 'user', content: '당신은 mlb전문가입니다' },
        // { role: 'assistant', content: '네, 맞습니다! 저는 MLB(메이저리그 베이스볼)와 관련된 모든 질문에 답변할 수 있습니다. 야구, 선수, 팀, 기록, 트레이드, 경기 일정 등 궁금한 점을 질문해 주세요! 다른 주제에 대한 질문은 답변할 수 없습니다.' },
        // { role: 'user', content: userQuestion }, // 여기에 실제 유저 질문이 들어갑니다. 예: '류현진의 현재 소속팀은?'
        // { role: 'assistant', content: '저는 MLB와 관련된 질문에만 답변할 수 있습니다. 야구 관련 질문을 해주세요!' }


       
                      { 
                role: 'system', 
                content: baseballPrompt 
              },
              { role: 'user', content: userQuestion }
        ];


   // 메시지 배열에 유저와 어시스턴트 메시지 추가
    while (userMessages.length != 0 || assistantMessages.length != 0) {
        if (userMessages.length != 0) {
            // messages.push(
            //     JSON.parse('{"role": "user", "content": "'+String(userMessages.shift()).replace(/\n/g,"")+'"}')
            // )
            messages.push(
            JSON.parse('{"role": "user", "content": "'+String(userMessages.shift()).replace(/\\/g, "\\\\").replace(/"/g, '\\"').replace(/\n/g, " ")+'"}')
       );
        }

        if (assistantMessages.length != 0) {
            messages.push(
                JSON.parse('{"role": "assistant", "content": "'+String(assistantMessages.shift()).replace(/\n/g,"")+'"}')
            )
        }
    }


  const completion = await openai.chat.completions.create({
    // model: 'text-davinci-002',
    // prompt: 'Say this is a test',
    // max_tokens: 6,
    // temperature: 0,
    
      // 필수
      messages: messages,
      model: 'gpt-4.1',
      // 설정
      max_tokens: 800,
      temperature: 0.9, // 더 다양한 응답을 위해 높임
      presence_penalty: 0.6, // 반복을 줄임
      frequency_penalty: 0.6, // 반복을 줄임
  });

  // let fortune = completion.choices
  // 응답의 첫번째 메시지의 내용 추출
  let fortune = completion.choices[0].message['content']

  
  console.log(fortune);


  // 🔧 수정: 응답 헤더에 명시적으로 CORS 추가
  // res.setHeader('Access-Control-Allow-Origin', 'https://chatmlb.pages.dev');
  // res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
  // res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');




  // main().catch(console.error);
  // 응답 전송
  res.json({"assistant" : fortune});
  





  // 에러 처리
 } catch (error) {
    console.error('서버 오류 발생:', error);

    // 🔧 수정: 에러 응답에도 CORS 헤더 추가
    // res.setHeader('Access-Control-Allow-Origin', 'https://chatmlb.pages.dev');
    // res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
    // res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');
    // res.setHeader('Access-Control-Allow-Credentials', 'true');


    res.status(500).send('서버 오류');
  }

})


// 서버 시작
// app.listen(3020, () => {
//   console.log('서버가 포트 3020에서 실행 중입니다.');
// });
module.exports.handler = serverless(app);


