목표
0. socket의 이벤트 처리는 어떻게 할건지.
1. 리스너와 세션 분리된 클래스
2. 싱글 쓰레드에서 => 멜티쓰레드, 멀티프로세스, 비동기
3. 세션 관리는 어디서 할지 제일 나중에 결정하자.

정리
리스너에서 accept 하면 session을 만들어준다.
기존에는 ISessionHandler에서 Session의 생성과 소명을 담당했다.
session은 연결,보냄,받기,종료,에러의 fn이벤트를 갖는다.
session에서 받기 구현 시 멀티 프로세스로 나중에 구현하자.
이것들을 하기 위해서는 socket의 비동기 이벤트 구조와 Thread에 대한 이해가 필요하다.
만약 C#처럼 newtask가 어렵다면 기존에 만들었던 것 처럼 message passing으로 만들어야 한다.
socket도 기본 비동기 라이브러리가 없다면 window iocp를 구현해야한다.
