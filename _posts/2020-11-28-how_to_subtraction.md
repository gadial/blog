---
title: "ארבע פעולות החשבון - חיסור"
layout: post
categories:
  - מספרים
tags:
  - חיבור
---

<a href="https://gadial.net/2020/11/18/how_to_addition/">בפוסט הקודם</a> דיברתי על פעולת ה<strong>חיבור</strong> של מספרים טבעיים והפעם אני רוצה לדבר על הפעולה ה"משלימה" לה - <strong>חיסור</strong>. למה אני אומר "משלימה"? כי אם חיבור עונה לנו על השאלה "לאן הגענו מ-{% equation %}a{% endequation %} אחרי שהלכנו עוד מרחק {% equation %}b{% endequation %}?" אז חיסור עונה לנו על השאלה "אם הגענו מ-{% equation %}a{% endequation %} אל {% equation %}b{% endequation %}, כמה הלכנו?". או במשוואה, אם חיבור עונה על השאלה מהו {% equation %}x{% endequation %} בביטוי {% equation %}a+b=x{% endequation %}, אז חיסור עונה על השאלה מהו {% equation %}x{% endequation %} בביטוי {% equation %}a+x=b{% endequation %}.

אפשר לתאר את זה גם בצורה ציורית: נניח שהייתה לנו קבוצה עם 7 איברים, ומהם מחקתי שלושה; כמה נשארו לנו?

<img src="{{site.baseurl}}{{site.post_images}}/2020/11/subtraction.png" alt=""/>

גם פה, יש לנו חיבור בתחפושת: זו השאלה המשלימה לשאלה כמה איברים אדומים צריך להוסיף לקבוצה הימנית כדי לקבל את הקבוצה השמאלית.

אפשר לתת לחיסור הגדרה פורמלית יותר אם מכניסים למשחק את <strong>המספרים השליליים</strong> ואז לחסר את {% equation %}b{% endequation %} מ-{% equation %}a{% endequation %} זה בסך הכל לחבר אל {% equation %}a{% endequation %} את <strong>המספר הנגדי</strong> שמתאים ל-{% equation %}b{% endequation %} (מה שאנחנו מסמנים בתור המספר {% equation %}-b{% endequation %}), אבל בפוסט הזה אני רוצה להתמקד במספרים הטבעיים אז לא ארחיב יותר על העניין הזה. הנקודה שצריך לזכור היא שחיסור הוא מושג שהיה קיים במשך אלפי שנים גם בלי להזדקק לקיום המספרים השליליים (שהפכו לחלק סטנדרטי מהמשחק המתמטי בשלב מאוחר יחסית) וגם אצל ילדים בימינו נלמד בדרך כלל עצמאית לפני שמגיעים אל השליליים; למעשה, השליליים נותנים לנו את התשובה לשאלה מה קורה אם מחסרים מ-{% equation %}a{% endequation %} מספר שגדול ממנו - אבל גם על זה אני לא הולך לדבר הפעם! (התשובה: אם {% equation %}b{% endequation %} גדול מ-{% equation %}a{% endequation %} אז אפשר לחשב קודם כל את {% equation %}b-a{% endequation %} ואז לקחת את המספר הנגדי לתוצאה שקיבלנו).

חיסור שונה מחיבור בכך שחוק החילוף וחוק הקיבוץ הנחמדים לא מתקיימים לנו: {% equation %}a-b\ne b-a{% endequation %} זה כמעט ברור ({% equation %}a-b{% endequation %} הוא הנגדי של {% equation %}b-a{% endequation %} כמו שאמרתי לפני רגע). את כשלון חוק הקיבוץ קל לראות עם דוגמא: {% equation %}\left(9-6\right)-3=3-3=0{% endequation %} ולעומת זאת {% equation %}9-\left(6-3\right)=9-3=6{% endequation %}. אם כן, כשיש שתי פעולות חיסור, הסוגריים חשובים.

השאלה האמיתית שאני רוצה לענות עליה בפוסט הזה, בדומה לפוסט הקודם, היא איך <strong>לחשב</strong> חיסור. כאן דווקא יש דמיון לא מבוטל לחיבור ולשיטת <strong>החיבור הארוך</strong> שהראיתי בפוסט הקודם, אבל הענינים טיפה יותר מסובכים.

ראשית, מה צריך לזכור בעל פה? פחות או יותר את התוצאות של חיסור מספר בין 0 ל-9 מכל אחד מהמספרים שגדולים ממנו בין 0 ל-19. למשל, לזכור ש-{% equation %}9-6=3{% endequation %} אבל גם ש-{% equation %}13-7=6{% endequation %}. אין לי טריק טוב איך לזכור את התוצאות הללו מלבד להתעסק איתן מספיק, אבל אפשר לבצע את החיסור הזה בראש בעזרת תשע אצבעות: כדי לחשב את {% equation %}13-7{% endequation %}, למשל, אני אזקוף 7 אצבעות, ואז אתחיל לקפל אותן ועל כל אצבע שאני מקפל אני ארד צעד אחד החל מ-13. כלומר אני אגיד "13" (כשיש לי 7 אצבעות מוצגות), "12" (אחרי שקיפלתי את הראשונה ונשארתי עם 6) וכך הלאה עד "6" (אחרי שקיפלתי את האצבע האחרונה).

בשביל לראות חיסור ארוך, בואו ניזכר איך עבד חיבור ארוך

{% equation %}\begin{array}{ccc}  & 5 & 3\\ + & 2 & 1\\ \hline  & 7 & 4 \end{array}{% endequation %}

הרעיון פה היה לכתוב את המספרים {% equation %}53{% endequation %} ו-{% equation %}21{% endequation %} זה מעל זה, ואז לעבור על הספרות שלהם <strong>מימין לשמאל</strong>, לחבר כל זוג ספרות ולכתוב את התוצאה למטה. זה עובד בדיוק באותו אופן גם עם חיסור:

{% equation %}\begin{array}{ccc}  & 5 & 3\\ - & 2 & 1\\ \hline  & 3 & 2 \end{array}{% endequation %}

{% equation %}3-1=2{% endequation %} ומכאן שהספרה הימנית בתוצאה היא 2, ואילו {% equation %}5-2=3{% endequation %} ומכאן שהספרה השמאלית בתוצאה היא 3. עד כאן הכל טוב. הסיבוך מתחיל כשהספרה העליונה <strong>קטנה יותר</strong> מהספרה התחתונה.

ראשית, בואו ניזכר מה עשיתי כשהיה סיבוך בחיבור. שם הסיבוך מגיע מסיבה שונה: מכך שסכום שתי הספרות הוא לפחות 10 ולכן לא ניתן לייצג אותו על ידי ספרה בודד. הטריק במקרה הזה היה "להגלות" את ספרת העשרות אל העמודה הבאה, שם היא תתווסף לחיבור:

{% equation %}\begin{array}{ccc}  & 1\\  & 5 & 3\\ + & 2 & 7\\ \hline  & 8 & 0 \end{array}{% endequation %}

כאן {% equation %}3+7=10{% endequation %} אז כתבנו את ה-0 בתור הספרה שלנו, ואת ה-1 העברנו הלאה, להתחבר עם ה-5 וה-2.

בחיסור התעלול הוא <strong>הפוך</strong>: במקום להוסיף 1 לסכום עבור הספרות שמשמאל, אנחנו <strong>מחסרים</strong> 1 מהן, כדי להוסיף לספרות שלנו 10 - אפשר לומר שאנחנו <strong>לווים</strong> משהו מהספרות שמשמאל. כדי לראות איך זה עובד, בואו נסתכל לרגע על הדוגמא {% equation %}53-27{% endequation %}: כאן אם נבצע את החיסור {% equation %}3-7{% endequation %} נקבל {% equation %}-4{% endequation %} וזו לא ספרה בין 0 ל-9. לכן אני משנה קצת את החשיבה שלי על התרגיל. במקום לומר ש-

{% equation %}53-27=\left(3-7\right)\cdot1+\left(5-2\right)\cdot10{% endequation %}

אני אומר לעצמי שאת ה-5 הזה אפשר לכתוב בתור {% equation %}\left(4+1\right)\cdot10{% endequation %} ואז את ה-{% equation %}1\cdot10{% endequation %} הזה אני יכול להוסיף אל החגיגה של {% equation %}\left(3-7\right)\cdot1{% endequation %}, ולקבל

{% equation %}53-27=\left(10+3-7\right)\cdot1+\left(4-2\right)\cdot10{% endequation %}

זה מה שעושים באופן כללי: בכל צעד של החיסור אנחנו מחסרים מהספרה העליונה את התחתונה. אם העליונה גדולה או שווה לתחתונה, הכל טוב. אם היא קטנה יותר, אנחנו מוסיפים לה 10 ומקטינים את הספרה העליונה שמשמאלה ב-1. ומה אם אין ספרה מצד שמאל? במקרה הזה יוצא שחיסרנו את המספר <strong>הגדול יותר</strong> מהקטן וזה לא הולך לעבוד - צריך לחסר את הקטן מהגדול.

עכשיו לשאלה המאתגרת באמת - איך <strong>כותבים</strong> את זה? ובכן, התשובה הנאיבית היא "מה שעובד לכם". הנה איך <strong>אני</strong> עושה חיסור כזה:

{% equation %}\begin{array}{ccc}  & 1\\  & 5 & 3\\ - & 2 & 7\\ \hline  & 2 & 6 \end{array}{% endequation %}

מה הולך פה? ראשית, אני מתרגם אוטומטית בראש את {% equation %}3-7{% endequation %} לכך שצריך לכתוב את הספרה 6 למטה (כלומר, עובר מלחשוב על 3 בתור {% equation %}3{% endequation %} אל לחשוב עליו בתור {% equation %}13{% endequation %}; ואם תרצו, אני מבצע <strong>חיסור מודולו </strong><strong>10</strong> בראש). שנית, אני בלי שום בושה כותב 1 מעל {% equation %}5{% endequation %} מתוך מוסכמה עם עצמי שאבין שצריך <strong>לחסר</strong> את ה-1 הזה מה-5, יחד עם ה-2 שאנחנו כבר ככה מחסרים ממנו. לרוב אני אפילו משמיט את כתיבת ה-1 הזה ופשוט <strong>זוכר</strong> שצריך לחסר 2 מ-4 במקום מ-5.

גישה אחרת היא פשוט <strong>למחוק</strong> את המספרים הסוררים ולכתוב גרסה תקינה שלהם (13 במקום 3, 4 במקום 5):

{% equation %}\begin{array}{ccc}  & 4 & 13\\  & \require{cancel}\cancel{5} & \require{cancel}\cancel{3}\\ - & 2 & 7\\ \hline  & 2 & 6 \end{array}{% endequation %}

זו נראית לי גישה טובה כדי לצמצם טעויות, לפחות עד שמתרגלים לטכניקה. היא כמובן די מכוערת, אבל אסתטיקה היא לא היעד שלנו בחיסור ארוך אלא להצליח לפתור את התרגיל!

ובכן, זה כל מה שהיה לי להגיד על חיסור - הכיף האמיתי יגיע בפוסט הבא, כשנגיע לכפל. 