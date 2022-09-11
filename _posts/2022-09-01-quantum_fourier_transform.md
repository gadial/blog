---
title: "התמרת פורייה הקוונטית"
layout: post
categories:
  - חישוב קוונטי
tags:
  - חישוב קוונטי
description: "התמרת פורייה היא כבר ככה קסם, אז רק לחשוב מה יקרה כשיעשו אותה קוונטית"
image: "2022/QFT_3_qubits.png"

---


<h2>מה זה בכלל ובשביל מה זה טוב?</h2>

בסדרת הפוסטים הקודמת שלי על חישוב קוונטי, מטרת העל שלי הייתה הגעה אל <strong>האלגוריתם של שור</strong>, לפירוק מהיר של מספרים לגורמים. בגלל ההשלכות המהותיות שיהיו לאלגוריתם הזה אם ימומש בפועל בצורה אמינה, הוא הפך להיות "הגביע הקדוש" של הצגה פופולרית של חישוב קוונטי - הפואנטה שמנסים להגיע אליה. וזה גרם לי קצת לרוץ על מה שקורה בדרך אליו, ובפרט דחסתי ב<a href="https://gadial.net/2014/08/24/shor_algorithm/">התחלה של הפוסט עליו</a> את הכלי המרכזי שעליו הוא מסתמך - <strong>התמרת פורייה המהירה</strong>. לכלי הזה מגיע פוסט משל עצמו, ועכשיו סוף סוף אתקן את המעוות.

"התמרת פורייה" היא קסם שמופיע בשלל מקומות ברחבי המתמטיקה. בגדול, הרעיון בה הוא לקחת פריט מידע כלשהו ולפרק אותו לגורמים שמאפשרים לראות דברים שחבויים לרוב מתחת לפני השטח. הדוגמא הקלאסית היא <strong>גל קול</strong>. התיאור הכללי של גל קול נותן את העוצמה שלו ("אמפליטודה") לאורך זמן. אם ניקח את גל הקול הזה ונבצע עליו התמרת פורייה, נקבל מעין פירוק שלו לאינספור גלים פשוטים, כאלו שאפשר לתאר בעזרת סינוסים וקוסינוסים, שמתאימים לתדירויות שונות ש"מתחבאות" בתוך גל הקול. אם גל הקול הוא של להקה, אז תדירויות שונות בפירוק הפורייה יתאימו לכלי נגינה שונים - יש תדירויות שמתאימות לסולנית, וכאלו שמתאימות לגיטרה בס, וכאלו שמתאימות לקלידים; ואם נחזק או נחליש תדירויות מסויימות, אז בגל הקול המקורי נשמע טוב יותר או פחות את כלי הנגינה המתאים. זה סוג של ניתוח שאפשר לבצע באמצעות התמרת פורייה שנותן אינטואיציה גם להפעלה שלה על תחומים שונים בעליל.

בפוסט הזה אני לא אכנס לשימושים - בפוסט הבא יופיע שימוש חזק מאוד, שנקרא <strong>הערכת פאזה</strong> והוא מה שמוביל גם לאלגוריתם של שור. אני אסתפק בלהציג את ההגדרות הפורמליות ואיך עושים את זה קוונטית.

<h2>מה זו התמרת פורייה?</h2>

יש לי סדרה של פוסטים על <a href="https://gadial.net/2014/04/28/fourier_series_intro/">התמרות פורייה</a> למיניהן, אז לא אכנס כאן לתיאור רחב של כל הסוגים שלהן והקשרים ביניהם (אבל יש הרבה סוגים ויש קשרים ביניהם וזה מגניב). מה שמעניין אותנו ספציפית בפוסט הזה הוא מה שנקרא <strong>התמרת פורייה הבדידה</strong> ומוגדר כך:

אם {% equation %}N{% endequation %} הוא מספר טבעי כלשהו ו-{% equation %}\left(a_{0},a_{1},\ldots,a_{N-1}\right)\in\mathbb{C}^{N}{% endequation %} היא סדרה של {% equation %}N{% endequation %} מספרים מרוכבים, אז התמרת פורייה הבדידה שלה היא סדרה אחרת של {% equation %}N{% endequation %} מספרים מרוכבים, {% equation %}\left(b_{0},\ldots,b_{N-1}\right){% endequation %} שמקיימת

{% equation %}b_{j}=\frac{1}{\sqrt{N}}\sum_{k=0}^{N-1}a_{k}e^{\frac{2\pi i}{N}jk}{% endequation %}

זו נוסחה טיפה מפחידה במבט ראשון ויהיה קריטי לנו להתרגל אליה, אז בואו נדבר שניה על מה זה {% equation %}e^{\frac{2\pi i}{N}jk}{% endequation %}. זו בסך הכל שיטת סימון למספר מרוכב מסוים, ולא סתם מספר מרוכב אלא <strong>שורש יחידה</strong> מסדר {% equation %}N{% endequation %}, כלומר מספר מרוכב {% equation %}z{% endequation %} שמקיים {% equation %}z^{N}=1{% endequation %}. למשל, שורשי היחידה מסדר 4 הם {% equation %}\left\{ 1,-1,i,-i\right\} {% endequation %}. אז התמרת פורייה הבדידה היא בסך הכל "כדי לקבל את האיבר ה-{% equation %}k{% endequation %} של ההתמרה, בואו נחבר את כל ה-{% equation %}a{% endequation %}-ים של הסדרה המקורית כשהם מוכפלים בשורשי יחידה מסויימים ש-{% equation %}k{% endequation %} מגדיר לנו". זה הכל, וזה לא כזה נורא מבחינה קונספטואלית.

איך כל זה קשור למספר {% equation %}e{% endequation %}? ובכן, אחת הנוסחאות הבסיסיות באנליזה מרוכבת היא <strong>נוסחת אוילר</strong>:

{% equation %}e^{i\theta}=\cos\theta+i\sin\theta{% endequation %}

על המספר המרוכב {% equation %}\cos\theta+i\sin\theta{% endequation %} אפשר לחשוב בתור נקודה במישור, עם קואורדינטות {% equation %}\left(\cos\theta,\sin\theta\right){% endequation %}; אם זוכרים ש-{% equation %}\cos^{2}\theta+\sin^{2}\theta=1{% endequation %} אז רואים שהמרחק של הנקודה הזו מראשית הצירים הוא 1, כך שאפשר לחשוב על כל הנקודות מהצורה הזו בתור <strong>מעגל</strong> - מעגל היחידה. הזווית {% equation %}\theta{% endequation %} היא הזווית שיוצר קו מראשית הצירים אל הנקודה הזו ביחס לכיוון החיובי של ציר {% equation %}x{% endequation %}.

<img src="{{site.baseurl}}{{site.post_images}}/2022/euler_formula.png" alt=""/>

לא כזה קריטי להבין מדוע הנוסחה הזו נכונה עכשיו - מבחינתנו אפשר לחשוב עליה בתור דרך קומפקטית לכתוב מספרים מרוכבים. מה שרלוונטי לנו הוא להבין מה קורה אם מציבים {% equation %}\theta=2\pi{% endequation %}. במקרה הזה, אפשר לחשוב על המספר בתור מה שמקבלים כשמתחילים על הנקודה {% equation %}\left(1,0\right){% endequation %} במישור ואז מבצעים סיבוב של {% equation %}2\pi{% endequation %} מעלות סביב ראשית הצירים. כזכור, {% equation %}2\pi{% endequation %} זו הדרך להגיד ברדיאנים את מה שנקרא "360 מעלות" בשפת בני אנוש - סיבוב שלם, שמחזיר אותנו אל {% equation %}\left(1,0\right){% endequation %}. שורשי היחידה הם מה שמקבלים כשלוקחים את הסיבוב השלם הזה וחותכים אותו לחתיכות מאורך שווה - למשל, שורשי היחידה מסדר 4 מתקבלים כשמחלקים את ה-360 מעלות הללו ל-4, ומקבלים סיבובים של 90 מעלות, או {% equation %}\frac{\pi}{2}{% endequation %} בשפת הרדיאנים. כך למשל {% equation %}i=e^{i\frac{\pi}{2}}{% endequation %}.

את הביטוי המפחיד {% equation %}e^{\frac{2\pi i}{N}jk}{% endequation %} אפשר להציג, אם כן, בתור דבר קצת יותר רגוע:

{% equation %}e^{\frac{2\pi i}{N}jk}=\left(e^{i\cdot\frac{2\pi}{N}k}\right)^{j}{% endequation %}

כלומר, כדי לחשב את {% equation %}b_{j}{% endequation %}, אנחנו קודם כל לוקחים את שורשי היחידה מסדר {% equation %}N{% endequation %}, שהם איברים מהצורה {% equation %}e^{i\cdot\frac{2\pi}{N}\cdot k}{% endequation %} עבור {% equation %}k=0,1,\ldots,N-1{% endequation %}, ואז אנחנו מעלים את כולם בחזקת {% equation %}j{% endequation %}, כופלים ב-{% equation %}a_{n}{% endequation %}-ים המתאימים ומחברים. למשל, עבור {% equation %}N=4{% endequation %}:

{% equation %}b_{j}=a_{0}\cdot1^{j}+a_{1}\cdot i^{j}+a_{2}\cdot\left(-1\right)^{j}+a_{3}\cdot\left(-i\right)^{j}{% endequation %}

זה יניב כל מני סכומים מורכבים יותר ופחות, כתלות בערך של {% equation %}k{% endequation %}. למשל עבור {% equation %}j=0{% endequation %} נקבל פשוט

{% equation %}b_{0}=\frac{1}{2}\left(a_{0}+a_{1}+a_{2}+a_{3}\right){% endequation %}

עבור {% equation %}j=1{% endequation %} כל שורשי היחידה השונים יככבו בסכום:

{% equation %}b_{1}=\frac{1}{2}\left(a_{0}+ia_{1}-a_{2}-ia_{3}\right){% endequation %}

עבור {% equation %}j=2{% endequation %} דברים הולכים להתבטל כי {% equation %}\left(-1\right)^{2}=1{% endequation %} ו-{% equation %}\left(\pm i\right)^{2}=-1{% endequation %}:

{% equation %}b_{2}=\frac{1}{2}\left(a_{0}-a_{1}+a_{2}-a_{3}\right){% endequation %}

וכן הלאה - אני מקווה שהעיקרון ברור.

החישוב של ההתמרה לא נראה פה כמו עניין קשה במיוחד, והוא באמת לא קשה במיוחד אם {% equation %}N{% endequation %} לא גדול. אבל אנחנו רוצים כן לטפל במקרה שבו {% equation %}N{% endequation %} גדול. חישוב נאיבי של ההתמרה לוקח בערך {% equation %}O\left(N^{2}\right){% endequation %} פעולות, אבל היופי בכל הסיפור הזה הוא שקיימות שיטות מחוכמות לביצוע <strong>מהיר</strong> של התמרת פורייה הזו, שלוקחות זמן של {% equation %}O\left(N\log N\right){% endequation %}. <a href="https://gadial.net/2014/05/27/fast_fourier_transform/">יש לי תיאור</a> של אחת מהשיטות הללו בבלוג וזה אכן יופי של דבר. כל הדברים הללו קשורים לחישוב <strong>קלאסי</strong>, בלי מחשב קוונטי.

בחישוב קוונטי אפשר לבצע את התמרת פורייה הזו בזמן {% equation %}O\left(\log^{2}N\right){% endequation %}. שימו לב להבדל: בהתמרה קלאסית, הזמן הוא {% equation %}O\left(N\log N\right){% endequation %}. בקוונטית הוא {% equation %}O\left(\log^{2}N\right){% endequation %}. זה שינוי עצום. אנחנו נעבוד עם המקרה שבו {% equation %}N=2^{n}{% endequation %} עבור {% equation %}n{% endequation %} כלשהו; במקרה הזה, {% equation %}O\left(\log^{2}N\right)=O\left(n^{2}\right){% endequation %} בזמן ש-{% equation %}O\left(N\log N\right)=O\left(n\cdot2^{n}\right){% endequation %} - אקספוננציאלי ב-{% equation %}n{% endequation %} מול פולינומי ב-{% equation %}n{% endequation %}. זו הדגמה יפה מאוד של הכוח של חישוב קוונטי ביחס לחישוב רגיל.

אבל מה? התמרת פורייה הקוונטית היא גם המחשה מצויינת ל<strong>חולשה</strong> של חישוב קוונטי אל מול חישוב רגיל. בחישוב רגיל, אנחנו מתחילים עם הסדרה {% equation %}a_{0},a_{1},\ldots,a_{N-1}{% endequation %} ביד ומסיימים עם הסדרה {% equation %}b_{0},b_{1},\ldots,b_{N-1}{% endequation %} ביד; לעומת זאת בחישוב קוונטי מה שיהיה לנו בסוף הוא <strong>סופרפוזיציה</strong> כלשהי של אברי הסדרה {% equation %}b_{0},b_{1},\ldots,b_{N-1}{% endequation %} (ההגדרה המדויקת תכף תגיע). אנחנו לא יודעים לקרוא את ה-{% equation %}b{% endequation %}-ים מתוך הסופרפוזיציה הזו; רק למדוד אותה ולקוות לטוב, או לעשות איתה עוד דברים בהמשך החישוב, ואז למדוד אותה ולקוות לטוב. ה"מידע" של התמרת הפורייה לא נגיש לנו ישירות, אלא רק דרך אפקט עקיף. כפי שנראה בהמשך, גם האפקט העקיף הזה יכול להיות חזק מאוד, בשימושים המתאימים.

<h2>איך נראית התמרת פורייה הקוונטית?</h2>

כאשר {% equation %}N=2^{n}{% endequation %}, התמרת פורייה הקוונטית היא אופרטור שפועל על {% equation %}n{% endequation %} קיוביטים. כזכור, המצב הכללי של {% equation %}n{% endequation %} קיוביטים הוא סופרפוזיציה מהצורה {% equation %}\sum_{x\in\left\{ 0,1\right\} ^{n}}\alpha_{x}\left|x\right\rangle {% endequation %}, כאשר ה-{% equation %}\left|x\right\rangle {% endequation %}-ים הללו הם אברי הבסיס של המצב הקוונטי. בשביל התמרת פורייה אנקוט בשיטת סימון טיפ-טיפה שונה: הרי על כל {% equation %}x\in\left\{ 0,1\right\} ^{n}{% endequation %} כזה אפשר לחשוב בתור <strong>ייצוג בינארי</strong> של מספר, למשל {% equation %}110{% endequation %} הוא הייצוג הבינארי של {% equation %}1\cdot2^{2}+1\cdot2^{1}+0\cdot2^{0}=6{% endequation %}. אז במקום לדבר על המצב {% equation %}\left|110\right\rangle {% endequation %} אני אדבר על המצב {% equation %}\left|6\right\rangle {% endequation %}. ובאופן כללי - המצבים שלי יהיו מהצורה {% equation %}\left|j\right\rangle {% endequation %} כאשר {% equation %}0\le j\le N-1{% endequation %}.

שימו לב כי בשיטת הייצוג הזו, הערך של הקיוביט הראשון הוא <strong>הספרה המשמעותית ביותר</strong> ב-{% equation %}j{% endequation %} והערך של הקיוביט האחרון הוא הספרה הכי פחות משמעותית; זו בחירה שרירותית, כמובן, אבל היא תשפיע על הסימונים שלנו מכאן ואילך.

כעת, כדי להגדיר אופרטור אוניטרי על {% equation %}n{% endequation %} קיוביטים, מספיק להגדיר אותו על אברי הבסיס. אז הבה ונגדיר את האופרטור {% equation %}\text{QFT}_{N}{% endequation %} (ראשי תיבות של Quantum Fourier Transform):

{% equation %}\text{QFT}_{N}\left(\left|j\right\rangle \right)=\frac{1}{\sqrt{N}}\sum_{k=0}^{N-1}e^{\frac{2\pi i}{N}jk}\left|k\right\rangle {% endequation %}

כלומר, אם אנחנו מפעילים את {% equation %}\text{QFT}_{N}{% endequation %} על סופרפוזיציה {% equation %}\sum_{j=0}^{N-1}a_{j}\left|j\right\rangle {% endequation %}, הפלט יהיה

{% equation %}\sum_{j=0}^{N-1}a_{j}\frac{1}{\sqrt{N}}\sum_{k=0}^{N-1}e^{\frac{2\pi i}{N}jk}\left|k\right\rangle =\sum_{k=0}^{N-1}\left(\frac{1}{\sqrt{N}}\sum_{j=0}^{N-1}a_{j}e^{\frac{2\pi i}{N}jk}\right)\left|k\right\rangle ={% endequation %}

{% equation %}=\sum_{k=0}^{N-1}b_{k}\left|k\right\rangle {% endequation %}

כלומר, כשמפעילים את {% equation %}\text{QFT}_{N}{% endequation %} על סופרפוזיציה שמקדמיה הם הסדרה {% equation %}\left(a_{0},a_{1},\ldots,a_{N-1}\right){% endequation %} מקבלים כפלט סופרפוזיציה שמקדמיה הם הסדרה {% equation %}\left(b_{0},\ldots,b_{N-1}\right){% endequation %}. כלומר, במקרה הזה גם סדרת הקלט וגם סדרת הפלט נתונות בצורה מובלעת; לא בתור קלט מפורש אלא בתור מקדמים של סופרפוזיציה.

ההגדרה {% equation %}\text{QFT}_{N}\left(\left|j\right\rangle \right)=\frac{1}{\sqrt{N}}\sum_{k=0}^{N-1}e^{\frac{2\pi i}{N}jk}\left|k\right\rangle {% endequation %} מתאימה להגדרה ה"קלאסית", ותהיה מוכרת ונעימה למי שרגילים להתמרת פורייה הבדידה. אבל יש עוד דרך לתאר את אגף ימין פה - לא בתור סכום של {% equation %}2^{n}{% endequation %} מצבים על {% equation %}n{% endequation %} קיוביטים, אלא בתור <strong>מכפלה טנזורית</strong> של {% equation %}n{% endequation %} מצבים, אחד לכל קיוביט. שיטת הייצוג הנוספת הזו תהיה חדשה גם למי שמכירים את התמרת פורייה, ובמבט ראשון היא תהיה <strong>מפחידה ביותר</strong>. כל כך מפחידה, עד שגם אני, כשכתבתי בעבר דברים על התמרת פורייה הקוונטית, ניסיתי בכוח להתחמק ממנה - עד שהגעתי לשימושים בפועל בה וזה התפוצץ לי בפרצוף. האמת היא ששיטת הייצוג הזו היא גם נוחה מאוד לשימוש וגם לא כזו נוראית, אחרי שמתרגלים אליה. ומכיוון שאני לא מאמין בלשמור אתכם במתח אני אציג אותה מייד, וננסה להבין מה הולך שם ולמה זה מתאים להגדרה ה"רגילה":

{% equation %}\text{QFT}_{N}\left(\left|j\right\rangle \right)\frac{1}{\sqrt{N}}\bigotimes_{t=1}^{n}\left(\left|0\right\rangle +e^{2\pi i0.j_{n-t+1}\ldots j_{n}}\left|1\right\rangle \right)={% endequation %}

{% equation %}=\frac{\left(\left|0\right\rangle +e^{2\pi i0.j_{n}}\left|1\right\rangle \right)\otimes\left(\left|0\right\rangle +e^{2\pi i0.j_{n-1}j_{n}}\left|1\right\rangle \right)\otimes\cdots\otimes\left(\left|0\right\rangle +e^{2\pi i0.j_{1}\ldots j_{n}}\left|1\right\rangle \right)}{\sqrt{N}}{% endequation %}

ככל הנראה הדבר הכי קשה לעיכול בנוסחה הזו הוא מה שקורה בחזקה של {% equation %}e{% endequation %}, אז אני אתחיל עם זה. בואו ננסה להבין איך נראה האיבר {% equation %}e^{\frac{2\pi i}{N}jk}{% endequation %} עבור {% equation %}j{% endequation %} כלשהו. נתחיל עם המקרה שבו {% equation %}k=1{% endequation %}. ראשית, אפשר לכתוב {% equation %}e^{\frac{2\pi i}{N}jk}=e^{2\pi i\cdot\frac{j}{N}}{% endequation %}, כלומר החלק שאנחנו צריכים להבין הוא את {% equation %}\frac{j}{N}{% endequation %}. שנית, אנחנו יודעים ש-{% equation %}0\le j\le N-1{% endequation %}, ולכן {% equation %}\frac{j}{N}{% endequation %} הולך להיות <strong>שבר</strong>: מספר בין 0 ל-1. מספרים כאלו אנחנו מייצגים בדרך כלל בייצוג עשרוני, נאמר {% equation %}0.125{% endequation %} בא לתאר את הסכום

{% equation %}1\cdot\frac{1}{10}+2\cdot\frac{1}{100}+5\cdot\frac{1}{1000}=\frac{125}{1000}=\frac{1}{8}{% endequation %}

כמו שאפשר לראות מהדוגמא, קל להבין איך ייראו הספרות של שבר כלשהו אם יש לנו הצגה שלו חלקי חזקה כלשהי של 10: מכיוון שהשבר שלנו היה מהצורה {% equation %}\frac{125}{1000}{% endequation %}, ידענו שהוא ייכתב בתור {% equation %}0.125{% endequation %}. אם אני מסתכל על השבר {% equation %}\frac{523}{1000}{% endequation %} אני כבר יודע שהוא ייכתב בתור {% equation %}0.523{% endequation %}.

ומה קורה אם אני רוצה להציג את המספר לא בשיטה העשרונית, אלא בשיטה <strong>הבינארית</strong>? בשיטה הזו אני עדיין יכול לכתוב ספרות שהן או 0 או 1 מימין לנקודה, ולקבל סכום של חזקות שליליות של 2. אם נסתכל על מספר עם שלוש ספרות מימין לנקודה, {% equation %}0.j_{1}j_{2}j_{3}{% endequation %}, הוא מייצג את

{% equation %}j_{1}\cdot\frac{1}{2^{-1}}+j_{2}+\frac{1}{2^{-2}}+j_{3}\cdot\frac{1}{2^{-3}}{% endequation %}

ובאופן כללי, {% equation %}0.j_{1}j_{2}\ldots j_{n}{% endequation %} הולך לייצג את {% equation %}\sum_{r=1}^{n}j_{r}\frac{1}{2^{r}}{% endequation %}. וכמו במקרה העשרוני, אם יש לי מספר שברי שמראש נתון בתור "משהו חלקי חזקה של 2", ברור לי איך ייראה הייצוג שלו: אם החזקה שבמכנה היא {% equation %}2^{n}{% endequation %}, אז אני אקח ייצוג בינארי שלו בעזרת {% equation %}n{% endequation %} ספרות, והן מה שיופיע מימין לנקודה. במילים אחרות, אם נתון לי {% equation %}\frac{j}{2^{n}}{% endequation %}, אז אני אכתוב את {% equation %}j{% endequation %} בתור {% equation %}j=\sum_{r=1}^{n}j_{r}2^{n-r}{% endequation %} (כלומר, כאן {% equation %}j_{1}{% endequation %} היא הספרה המשמעותית ביותר, {% equation %}j_{2}{% endequation %} הבאה בתור אחריה וכן הלאה; לרוב אנחנו עושים ההפך ולכן זו עשויה להיות נקודה מבלבלת). ואז אני אקבל את הייצוג הבינארי השברי

{% equation %}\frac{j}{2^{n}}=0.j_{1}j_{2}\ldots j_{n}{% endequation %}

אם הנקודה הזו (שלא קשורה לקוונטים או לאלגברה לינארית, סתם לייצוג של מספרים בבסיסי ספירה שונים) ברורה לכם - ברכותי! אני מקווה שהרע ביותר כבר מאחורינו.

עכשיו, מה קורה אם אני לוקח את המספר {% equation %}\frac{j}{2^{n}}=0.j_{1}j_{2}\ldots j_{n}{% endequation %} ומכפיל אותו פי 2? כמו שהכפלת ייצוג עשרוני רגיל ב-10 מזיזה את כל הספרות צעד אחד שמאלה, למשל {% equation %}10\cdot0.125=1.25{% endequation %}, אז גם בייצוג בינארי כל הספרות יזוזו צעד אחד שמאלה: 

{% equation %}2\cdot\frac{j}{2^{n}}=j_{1}.j_{2}j_{3}\ldots j_{n}{% endequation %}.

ובאופן כללי, אם אנחנו כופלים בחזקה כלשהי של 2, נאמר {% equation %}2^{t}{% endequation %} כאשר {% equation %}t\le n{% endequation %}, האפקט יהיה הזזת הספרות {% equation %}t{% endequation %} צעדים שמאלה:

{% equation %}2^{t}\cdot\frac{j}{2^{n}}=j_{1}j_{2}\ldots j_{t}.j_{t+1}\ldots j_{n}{% endequation %}.

אוקיי, התרגלנו קצת לצורת הכתיב הזו. עכשיו מגיע הפאנץ'. בואו נחזור שניה אל הביטוי {% equation %}e^{\frac{2\pi i}{N}jk}{% endequation %} שכבר ראינו לא מעט כאן. אני יכול לכתוב אותו שוב פעם באופן קצת שונה: {% equation %}e^{2\pi i\cdot\left(k\cdot\frac{j}{N}\right)}{% endequation %}. כעת, מכיוון שאצלנו {% equation %}N=2^{n}{% endequation %} אפשר לכתוב אותו בתור

{% equation %}e^{2\pi i\cdot\left(k\cdot\frac{j}{2^{n}}\right)}{% endequation %}

ואם נניח ש-{% equation %}k{% endequation %} הוא חזקה כלשהי של 2, נאמר {% equation %}k=2^{n-t}{% endequation %} (למה לא {% equation %}k=2^{t}{% endequation %}? כי דווקא בראשון נשתמש בהמשך), אז אפשר לכתוב

{% equation %}k\cdot\frac{j}{2^{n}}=j_{1}j_{2}\ldots j_{n-t}.j_{n-t+1}\ldots j_{n}{% endequation %}

ועכשיו הפאנץ': את כל החלק שמשמאל לנקודה הבינארית <strong>אנחנו יכולים להעלים</strong>. למה? בגלל שיש לנו אקספוננט בחזקת {% equation %}2\pi i{% endequation %} כפול משהו. בואו נראה את זה: אם יש לי מספר מהצורה {% equation %}a+b{% endequation %} כך ש-{% equation %}a{% endequation %} הוא מספר שלם, אז מתקיים

{% equation %}e^{2i\pi\left(a+b\right)}=e^{2i\pi a}\cdot e^{2i\pi b}=\left(e^{2i\pi}\right)^{a}\cdot e^{2i\pi b}=1\cdot e^{2i\pi b}=e^{2i\pi b}{% endequation %}

כלומר, כל החלק של {% equation %}a{% endequation %} נעלם, כי הוא מייצג כמות שלמה של סיבובים מלאים סביב ראשית הצירים, שלא משפיעה על התוצאה הסופית. איפה היה חשוב ש-{% equation %}a{% endequation %} הוא שלם? במעבר {% equation %}e^{2i\pi a}=\left(e^{2i\pi}\right)^{a}{% endequation %} שאינו נכון באופן כללי אבל כן נכון עבור שלמים.

חזרה אל המקרה שלנו, שבו יש לנו מספר בייצוג בינארי שאפשר להפריד לסכום של "מה שמשמאל לנקודה" ו"מה שמימין לנקודה":

{% equation %}k\cdot\frac{j}{2^{n}}=j_{1}j_{2}\ldots j_{n-t}.j_{n-t+1}\ldots j_{n}=j_{1}j_{2}\ldots j_{n-t}+0.j_{n-t+1}\ldots j_{n}{% endequation %}

ולכן נקבל, עבור {% equation %}k=2^{n-t}{% endequation %}, שמתקיים 

{% equation %}e^{2\pi i\cdot\left(k\cdot\frac{j}{2^{n}}\right)}=e^{2\pi i0.j_{n-t+1}\ldots j_{n}}{% endequation %}

וזה בדיוק מה שהופיע בנוסחה המוזרה של {% equation %}\text{QFT}{% endequation %} שנתתי:

{% equation %}\text{QFT}_{N}\left(\left|j\right\rangle \right)\frac{1}{\sqrt{N}}\bigotimes_{t=1}^{n}\left(\left|0\right\rangle +e^{2\pi i0.j_{n-t+1}\ldots j_{n}}\left|1\right\rangle \right){% endequation %}

כלומר, הבנו את המשמעות של הרכיב הכי בעייתי בנוסחה; עכשיו בואו נבין למה היא נכונה ושקולה אל

{% equation %}\text{QFT}_{N}\left(\left|j\right\rangle \right)=\frac{1}{\sqrt{N}}\sum_{k=0}^{N-1}e^{\frac{2\pi i}{N}jk}\left|k\right\rangle {% endequation %}

אין כאן יותר מאשר חישוב טכני. אני לא אוהב דברים שאין בהם יותר מאשר חישוב טכני. קשה לפתח ככה אינטואיציה, והרבה ספרים פשוט נותנים את החישוב הטכני וזהו. אז לפני שנעשה את החישוב הטכני, בואו נראה דוגמא קצת יותר פשוטה: הפולינום {% equation %}\left(1+x\right)\left(1+x^{2}\right)\left(1+x^{3}\right){% endequation %}.

נניח שנותנים לנו את הפולינום הזה ומבקשים מאיתנו לפתוח סוגריים. זה יהיה טכני, אין ספק, אבל מה בעצם נעשה? אנחנו בעצם יוצרים 8 שלשות: כל שלשה נבנית על ידי כך שאני בוחר איבר מהסוגריים הראשונים, איבר מהשניים ואיבר מהשלישיים, וכופל את כולם. את כל 8 התוצאות שאקבל אני מחבר. עכשיו, בגלל שבכל אחד מהסוגריים אחד האיברים הוא 1, הכפלה בו לא עושה כלום, מה שדי מפשט את מה שאני מקבל:

{% equation %}1+x+x^{2}+x^{3}+x\cdot x^{2}+x\cdot x^{3}+x^{2}\cdot x^{3}+x\cdot x^{2}+x^{3}={% endequation %}

{% equation %}=1+x+x^{2}+x^{3}+x^{3}+x^{4}+x^{5}+x^{6}{% endequation %}

עכשיו אפשר לעשות את אותו דבר עם המכפלה הטנזורית שלנו:

{% equation %}\bigotimes_{t=1}^{n}\left(\left|0\right\rangle +e^{2\pi i0.j_{n-t+1}\ldots j_{n}}\left|1\right\rangle \right){% endequation %}

כזכור, מה שיפה במכפלות טנזוריות הוא שהן משחקות יפה עם חוקי הכפל והחיבור הרגילים. אם למשל יש לי את המכפלה הפשוטה יחסית

{% equation %}\left(\left|0\right\rangle +a\left|1\right\rangle \right)\otimes\left(\left|0\right\rangle +b\left|1\right\rangle \right){% endequation %}

ואני פותח את המכפלה על פי חוקי הדיסטריביוטיביות, <a href="https://gadial.net/2022/07/31/quantum_computing_math_2/">כמו שכבר ראינו</a> שאפשר לעשות במהלך סדרת הפוסטים הזו, אז אני אקבל

{% equation %}\left|00\right\rangle +b\left|01\right\rangle +a\left|10\right\rangle +ab\left|11\right\rangle {% endequation %}

כלומר, על ידי התבוננות בספרות של {% equation %}\left|x\right\rangle {% endequation %} אני יודע אילו איברים יופיעו במקדם של האיבר הזה: אם הספרה השמאלית, המשמעותית יותר, היא 1 אז יופיע {% equation %}a{% endequation %}, ואם הספרה הימנית היא 1 אז יופיע {% equation %}b{% endequation %}, ואם שתיהן 1 אז שניהם יופיעו. אותו הדבר יקרה גם עבור הביטוי

{% equation %}\bigotimes_{t=1}^{n}\left(\left|0\right\rangle +e^{2\pi i0.j_{n-t+1}\ldots j_{n}}\left|1\right\rangle \right){% endequation %}

כשאני אפתח אותו, אני אקבל סכום של כל האיברים מהצורה {% equation %}\left|x\right\rangle {% endequation %} כך של-{% equation %}x{% endequation %} יש {% equation %}n{% endequation %} ספרות, והמקדמים של ה-{% equation %}\left|x\right\rangle {% endequation %} הזה יהיו מכפלות של כל ה-{% equation %}e{% endequation %}-ים המפלצתיים שמתאימים לכניסות של {% equation %}x{% endequation %} שהן 1.

עכשיו, כשאני מרגיש שהבנו קצת יותר טוב מה הולך ב"ביטוי המפלצתי", אני דווקא רוצה לחזור אל ההגדרה ה"רגילה" של ההתמרה:

{% equation %}\text{QFT}_{N}\left(\left|j\right\rangle \right)=\frac{1}{\sqrt{N}}\sum_{k=0}^{N-1}e^{\frac{2\pi i}{N}jk}\left|k\right\rangle {% endequation %}

ובואו ננסה להגיע ממנה אל "הביטוי המפלצתי". הדבר היחיד בהגדרה הרגילה שעדיין לא מסתדר לנו טוב הוא ה-{% equation %}k{% endequation %} הזה. כזכור, הפישוט המאוד נחמד של {% equation %}e^{2\pi i\cdot\left(k\cdot\frac{j}{2^{n}}\right)}{% endequation %} שעשיתי קודם שבו נפטרתי מכל הספרות משמאל לנקודה הניח ש-{% equation %}k{% endequation %} הוא <strong>חזקה של </strong><strong>2</strong> וזה בוודאי לא מה שקורה כשמריצים את {% equation %}k{% endequation %} על כל המספרים מ-0 עד {% equation %}N-1{% endequation %}. כדי להתמודד עם הבעיה הזו, אנחנו עוברים להתבונן על <strong>הייצוג הבינארי</strong> של {% equation %}k{% endequation %}. מכיוון ש-{% equation %}0\le k\le N-1=2^{n}-1{% endequation %} אפשר לייצג את {% equation %}k{% endequation %} בעזרת {% equation %}n{% endequation %} ספרות בינאריות. נכתוב {% equation %}k=k_{1}k_{2}\ldots k_{n}{% endequation %}, כלומר שוב ה-{% equation %}k_{1}{% endequation %} יהיה הספרה המשמעותית ביותר, מה שאומר שבייצוג בתור סכום נקבל

{% equation %}k=\sum_{t=1}^{n}2^{n-t}k_{t}{% endequation %}

זוכרות שקודם מתישהו כפלתי ב-{% equation %}2^{n-t}{% endequation %} במקום ב-{% equation %}2^{t}{% endequation %} שנראה יותר טבעי? אז הנה איך {% equation %}2^{n-t}{% endequation %} צץ לו.

עכשיו אפשר להתחיל לעשות חשבון:

{% equation %}\text{QFT}_{N}\left(\left|j\right\rangle \right)=\frac{1}{\sqrt{N}}\sum_{k=0}^{N-1}e^{\frac{2\pi i}{N}jk}\left|k\right\rangle ={% endequation %}

{% equation %}=\frac{1}{\sqrt{N}}\sum_{k_{1}k_{2}\ldots k_{n}=0}^{N-1}e^{\frac{2\pi i}{N}j\sum_{t=1}^{n}2^{n-t}k_{t}}\left|k_{1}\ldots k_{n}\right\rangle ={% endequation %}

{% equation %}\frac{1}{\sqrt{N}}\sum_{k_{1}k_{2}\ldots k_{n}=0}^{N-1}\prod_{t=1}^{n}e^{\frac{2\pi i}{N}j2^{n-t}k_{t}}\left|k_{1}\ldots k_{n}\right\rangle ={% endequation %}

כשהמעבר האחרון נובע מכך שחיבור במעריך של {% equation %}e{% endequation %} הופך למכפלה, כמו בנוסחה {% equation %}e^{a+b}=e^{a}\cdot e^{b}{% endequation %}.

נעצור עכשיו לשניה ונסתכל על מה שהולך במעריך של ה-{% equation %}e{% endequation %} הזה: אם {% equation %}k_{t}=0{% endequation %}, אז {% equation %}e^{\frac{2\pi i}{N}j2^{n-t}k_{t}}=e^{0}=1{% endequation %} - המקדם נעלם כולו. אם לעומת זאת {% equation %}k_{t}=1{% endequation %} אנחנו נשארים עם {% equation %}e^{\frac{2\pi i}{N}j2^{n-t}}=e^{2\pi i\cdot0.0.j_{n-t+1}\ldots j_{n}}{% endequation %} שכבר מוכרים לנו בשלב הזה. אם כן, הדבר העיקרי שאנחנו צריכים לעשות עכשיו הוא לעבור מסכום של {% equation %}N{% endequation %} מכפלות של {% equation %}n{% endequation %} איברים אל מכפלה הטנזורית של {% equation %}n{% endequation %} איברים שכל אחד מהם הוא סכום של שניים:

{% equation %}\frac{1}{\sqrt{N}}\sum_{k_{1}k_{2}\ldots k_{n}=0}^{N-1}\prod_{t=1}^{n}e^{\frac{2\pi i}{N}j2^{n-t}k_{t}}\left|k_{1}\ldots k_{n}\right\rangle ={% endequation %}

{% equation %}=\frac{1}{\sqrt{N}}\bigotimes_{t=1}^{n}\left(e^{\frac{2\pi i}{N}j2^{n-t}\cdot0}\left|0\right\rangle +e^{\frac{2\pi i}{N}j2^{n-t}\cdot1}\left|1\right\rangle \right){% endequation %}

ועל פי הפישוטים שהראיתי לפני רגע, אנחנו מקבלים

{% equation %}\frac{1}{\sqrt{N}}\bigotimes_{t=1}^{n}\left(e^{\frac{2\pi i}{N}j2^{n-t}\cdot0}\left|0\right\rangle +e^{\frac{2\pi i}{N}j2^{n-t}\cdot1}\left|1\right\rangle \right)={% endequation %}

{% equation %}=\frac{1}{\sqrt{N}}\bigotimes_{t=1}^{n}\left(\left|0\right\rangle +e^{2\pi i0.j_{n-t+1}\ldots j_{n}}\left|1\right\rangle \right){% endequation %}

וזו בדיוק הנוסחה שרצינו. זהו, החלק הגרוע ביותר הסתיים - עכשיו אנחנו יודעים איך התמרת הפורייה הקוונטית נראית בצורה שלה שתהיה לנו שימושית יותר, וגם יהיה לנו יחסית קל להבין למה המעגל הקוונטי שתכף אתאר מחשב אותה. יש רק עוד פישוט אחד אחרון שאולי כדאי לעשות: מכיוון ש-{% equation %}N=2^{n}{% endequation %} הרי שאפשר לכתוב {% equation %}\sqrt{N}=2^{\frac{n}{2}}{% endequation %} ולקבל את הנוסחה

{% equation %}\frac{1}{2^{n/2}}\bigotimes_{t=1}^{n}\left(\left|0\right\rangle +e^{2\pi i0.j_{n-t+1}\ldots j_{n}}\left|1\right\rangle \right){% endequation %}

ולפעמים אפילו כותבים

{% equation %}\bigotimes_{t=1}^{n}\frac{1}{\sqrt{2}}\left(\left|0\right\rangle +e^{2\pi i0.j_{n-t+1}\ldots j_{n}}\left|1\right\rangle \right){% endequation %}

בתור התמרת פורייה הקוונטית. אני אישית מאוד מחבב את הצורה האחרונה, כי אחרי שמתעסקים מספיק זמן עם חישוב קוונטי כבר מתרגלים לאהוב {% equation %}\sqrt{2}{% endequation %} מוזרים שנדחפים לכל מקום, וכפי שנראה עוד רגע - זו גם תהיה הצורה הכי מועילה עבורנו.

<h2>אז איך מחשבים את זה?</h2>

סיכום החלק הקודם הוא פשוט: אנחנו רוצים לממש אופרטור קוונטי בשם {% equation %}\text{QFT}_{N}{% endequation %} שמקיים

{% equation %}\text{QFT}_{N}\left(\left|j\right\rangle \right)=\bigotimes_{t=1}^{n}\frac{1}{\sqrt{2}}\left(\left|0\right\rangle +e^{2\pi i0.j_{n-t+1}\ldots j_{n}}\left|1\right\rangle \right){% endequation %}

הייצוג באגף ימין, שנראה אולי מפחיד בהתחלה, מועיל <strong>מאוד</strong> להבין מה צריך לעשות, כי זה ייצוג של מצב קוונטי בצורה פשוטה מאוד, שבה המצב של כל קיוביט מתואר <strong>בנפרד</strong>. זה לא מצב שזור; כדי להבין איך מגיעים אליו מספיק להסתכל על כל קיוביט בתורו.

ראשית, בואו ניזכר בזהירות מה <strong>הקלט</strong> שלנו פה. יש למעגל {% equation %}n{% endequation %} קיוביטים, והמצב שלהם הוא {% equation %}\left|j\right\rangle {% endequation %}, שאותו אני מתאר בתור {% equation %}\left|j_{1}j_{2}\ldots j_{n}\right\rangle {% endequation %} - כל {% equation %}j_{t}{% endequation %} כאן הוא או 0 או 1.

עכשיו, בואו נתחיל מהערך שאמור להגיע אל הקיוביט <strong>הראשון</strong>. כלומר, בנוסחה לעיל זה המקרה {% equation %}t=1{% endequation %} - המצב הבא:

{% equation %}\frac{1}{\sqrt{2}}\left(\left|0\right\rangle +e^{2\pi i0.j_{n}}\left|1\right\rangle \right){% endequation %}

זה מצב פשוט מאוד, אבל הוא מסווה את זה היטב עם השימוש הזה ב-{% equation %}e{% endequation %}. בואו נראה את זה: ל-{% equation %}j_{n}{% endequation %} יש בדיוק שני ערכים אפשריים: או 0 או 1. אם {% equation %}j_{n}=0{% endequation %} אז {% equation %}e^{2\pi i0.j_{n}}=1{% endequation %} ולכן המצב הוא {% equation %}\frac{\left|0\right\rangle +\left|1\right\rangle }{\sqrt{2}}{% endequation %}. אם לעומת זאת {% equation %}j_{n}=1{% endequation %} אז {% equation %}0.j_{n}=\frac{1}{2}{% endequation %} (זכרו - {% equation %}0.j_{n}{% endequation %} הוא לא ייצוג עשרוני אלא ייצוג בינארי) ולכן {% equation %}e^{2\pi i0.j_{n}}=e^{\pi i}=-1{% endequation %} (סיבוב של 180 מעלות) ונקבל {% equation %}\frac{\left|0\right\rangle -\left|1\right\rangle }{\sqrt{2}}{% endequation %}.

אז במילים אחרות, המצב שצריך לקבל תלוי בערך של {% equation %}j_{n}{% endequation %}, והוא

{% equation %}\begin{cases} \frac{\left|0\right\rangle +\left|1\right\rangle }{\sqrt{2}} & j_{n}=0\\ \frac{\left|0\right\rangle -\left|1\right\rangle }{\sqrt{2}} & j_{n}=1 \end{cases}{% endequation %}

נראה מוכר? המצב הזה הוא <strong>בדיוק</strong> התוצאה של {% equation %}H\left(\left|j_{n}\right\rangle \right){% endequation %}. ככה {% equation %}H{% endequation %} מוגדר. אז ברור לנו מה לעשות - כדי לקבל את הערך שאמור להגיע אל הקיוביט <strong>הראשון</strong> אנחנו רק צריכים להפעיל {% equation %}H{% endequation %} על הקיוביט {% equation %}\left|j_{n}\right\rangle {% endequation %}, כלומר על הקיוביט <strong>האחרון</strong>. רגע רגע רגע, משהו לא מסתדר פה.

תזכרו - אם אנחנו מפעילים {% equation %}H{% endequation %} על הקיוביט <strong>האחרון</strong> אנחנו משנים את הקיוביט <strong>האחרון</strong>. זה מה ששערים עושים - משנים את הקיוביט שעליו הם מופעלים. אז מה נעשה? פשוט מאוד: נפעיל את {% equation %}H{% endequation %} על הקיוביט האחרון. למעשה, כל מה שיקרה מעתה ואילך הולך לייצר לנו את הפלטים <strong>בסדר הפוך</strong> ממה שרצינו בהתחלה. זה לא נורא, כי אחרי שמסיימים לייצר את המצב שרצינו רק עם סדר קיוביטים הפוך, אפשר להפעיל שערי SWAP שמחליפים את הקיוביטים.

פורמלית, שער SWAP על שני קיוביטים מוגדר כך:

{% equation %}\text{SWAP}\left(\left|00\right\rangle \right)=\left|00\right\rangle {% endequation %}

{% equation %}\text{SWAP}\left(\left|01\right\rangle \right)=\left|10\right\rangle {% endequation %}

{% equation %}\text{SWAP}\left(\left|10\right\rangle \right)=\left|01\right\rangle {% endequation %}

{% equation %}\text{SWAP}\left(\left|11\right\rangle \right)=\left|11\right\rangle {% endequation %}

אם נפעיל אותו על שני קיוביטים לא שזורים, שאחד במצב {% equation %}\alpha\left|0\right\rangle +\beta\left|1\right\rangle {% endequation %} והשני במצב {% equation %}\gamma\left|0\right\rangle +\delta\left|1\right\rangle {% endequation %}, כלומר הם במצב המשותף

{% equation %}\left(\alpha\left|0\right\rangle +\beta\left|1\right\rangle \right)\otimes\left(\gamma\left|0\right\rangle +\delta\left|1\right\rangle \right)=\alpha\gamma\left|00\right\rangle +\alpha\delta\left|01\right\rangle +\beta\gamma\left|10\right\rangle +\beta\delta\left|11\right\rangle {% endequation %}

נגיע אל המצב

{% equation %}\alpha\gamma\left|00\right\rangle +\beta\gamma\left|01\right\rangle +\alpha\delta\left|10\right\rangle +\beta\delta\left|11\right\rangle =\left(\gamma\left|0\right\rangle +\delta\left|1\right\rangle \right)\otimes\left(\alpha\left|0\right\rangle +\beta\left|1\right\rangle \right){% endequation %}

כלומר, זה ישיג בדיוק את האפקט שרצינו, של החלפת הקיוביטים. איך אפשר לממש {% equation %}\text{SWAP}{% endequation %} שכזה? אפשר כמובן לעשות את זה כבר ברמת החומרה של המחשב הקונטי, אבל אפשר גם להשתמש בשלושה שערי {% equation %}\text{CX}{% endequation %} בזה אחר זה: 

{% equation %}\text{SWAP}_{1,2}=\text{CX}_{1,2}\text{CX}_{2,1}\text{CX}_{1,2}{% endequation %}

<img src="{{site.baseurl}}{{site.post_images}}/2022/swap_gate.png" alt=""/>

עשו את החישוב בעצמכם על ארבעת אברי הבסיס ותראו שהבניה הזו אכן עובדת. אז שערי SWAP הם לא בעיה משמעותית, ומעתה ואילך נמשיך לבנות את המעגל של התמרת הפורייה הקוונטית בלי לחשוש מכך שהוא מייצר לנו את הפלטים בסדר הפוך.

נעבור עכשיו אל המצב השני שצריך לייצר: {% equation %}\frac{1}{\sqrt{2}}\left(\left|0\right\rangle +e^{2\pi i0.j_{n-1}j_{n}}\left|1\right\rangle \right){% endequation %}. כאן הסיפור כבר מסתבך כי בחזקה של {% equation %}e{% endequation %} מעורבות <strong>שתי</strong> ספרות של {% equation %}j{% endequation %}, גם {% equation %}j_{n}{% endequation %} וגם {% equation %}j_{n-1}{% endequation %}. אם קודם פעלנו על הקיוביט {% equation %}\left|j_{n}\right\rangle {% endequation %}, עכשיו אנחנו רוצים לפעול על {% equation %}\left|j_{n-1}\right\rangle {% endequation %}, אבל מכיוון שהמצב שאנחנו צריכים להגיע אליו מערב גם את {% equation %}j_{n}{% endequation %} ברור שהקיוביט {% equation %}\left|j_{n}\right\rangle {% endequation %} צריך להשפיע איכשהו. ההשפעה שלו תבוא לידי ביטוי בכך שנפעיל על {% equation %}\left|j_{n-1}\right\rangle {% endequation %} שער <strong>מותנה</strong>, כלומר כזה שמופעל אם {% equation %}j_{n}=1{% endequation %} ולא מופעל אם {% equation %}j_{n}=0{% endequation %}. בשביל שזה יעבוד כמו שצריך, השער המותנה הזה צריך להיות מופעל <strong>לפני</strong> שאנחנו עושים את ה-{% equation %}H{% endequation %} על {% equation %}\left|j_{n}\right\rangle {% endequation %}, אחרת נקבל סמטוחה; זכרו שכדי לייצר מצב שזור (שזה <strong>לא</strong> מה שאנחנו רוצים פה!) מפעילים {% equation %}H{% endequation %} על קיוביט כלשהו ואז {% equation %}CX{% endequation %} על קיוביט אחר, כך שה-{% equation %}CX{% endequation %} מותנה בקיוביט שהפעלנו עליו {% equation %}H{% endequation %}. כלומר, מה שאני מתאר עכשיו הולך לקרות <strong>לפני</strong> הפעלת ה-{% equation %}H{% endequation %} על {% equation %}\left|j_{n}\right\rangle {% endequation %} (לא לדאוג! עוד מעט אראה דוגמא של המעגל השלם עבור שלושה קיוביטים ואז הכל יהיה ברור).

עכשיו, בואו ננסה להבין מה אנחנו רוצים לעשות לקיוביט {% equation %}\left|j_{n-1}\right\rangle {% endequation %}. אנחנו רוצים לייצר ממנו את {% equation %}\left|0\right\rangle +e^{2\pi i0.j_{n-1}j_{n}}\left|1\right\rangle {% endequation %}, כלומר ליצור סופרפוזיציה, כשבסופרפוזיציה הזו לא מתעסקים עם {% equation %}\left|0\right\rangle {% endequation %} אבל כן מתעללים קשות במקדם של {% equation %}\left|1\right\rangle {% endequation %}. ראינו ש-{% equation %}H{% endequation %} שמופעל על {% equation %}\left|j_{n-1}\right\rangle {% endequation %} הוא בעל אפקט כזה: הוא עוזב את {% equation %}\left|0\right\rangle {% endequation %} בשקט אבל כופל את המקדם של {% equation %}\left|1\right\rangle {% endequation %} ב-{% equation %}e^{2\pi i\cdot0.j_{n-1}}{% endequation %}. עכשיו, מה עם {% equation %}j_{n}{% endequation %}? ובכן, יש לנו פה את הסיטואציה הרגילה שסכום במעריך הופך למכפלה:

{% equation %}e^{2\pi i0.j_{n-1}j_{n}}=e^{2\pi i\left(0.j_{n-1}+0.0j_{n}\right)}=e^{2\pi i0.j_{n-1}}\cdot e^{2\pi i0.0j_{n}}{% endequation %}

כלומר, אנחנו רוצים להפעיל על המצב הקוונטי ש-{% equation %}\left|j_{n-1}\right\rangle {% endequation %} הולך אליו שער שכופל ב-1 אם {% equation %}j_{n}=0{% endequation %}, אז אם {% equation %}j_{n}=1{% endequation %} אז הוא כופל ב-

{% equation %}e^{2\pi i\cdot0.01}=e^{\frac{2\pi i}{4}}{% endequation %}

גם זה שער מוכר לנו: {% equation %}e^{\frac{2\pi i}{4}}=e^{\frac{\pi i}{2}}=i{% endequation %}, ולכן השער שרוצים לכפול בו הוא {% equation %}S{% endequation %}:

{% equation %}S=\left(\begin{array}{cc} 1 & 0\\ 0 & i \end{array}\right){% endequation %}

אבל ה-{% equation %}S{% endequation %} הזה, שמופעל על {% equation %}\left|j_{n-1}\right\rangle {% endequation %}, צריך להיות מותנה ב-{% equation %}\left|j_{n}\right\rangle {% endequation %}. איך מייצרים שער מותנה? <a href="https://gadial.net/2022/08/03/quantum_computing_math_4/">כבר תיארתי את זה</a> בפוסט על שערים קוונטיים: אם רוצים ליצור גרסה מותנית של האופרטור {% equation %}U{% endequation %} מסתכלים על מטריצת הבלוקים

{% equation %}\left(\begin{array}{cc} I & 0\\ 0 & U \end{array}\right){% endequation %}

כלומר, במקרה הנוכחי מפעילים את האופרטור 

{% equation %}\left(\begin{array}{cccc} 1 & 0 & 0 & 0\\ 0 & 1 & 0 & 0\\ 0 & 0 & 1 & 0\\ 0 & 0 & 0 & i \end{array}\right){% endequation %}

וזהו, זה משיג את האפקט שרצינו ואנו מקבלים {% equation %}\left|0\right\rangle +e^{2\pi i0.j_{n-1}j_{n}}\left|1\right\rangle {% endequation %}.

עוד צעד אחד וכבר נבין מה קורה באופן כללי: עכשיו אנחנו רוצים לייצר מ-{% equation %}\left|j_{n-2}\right\rangle {% endequation %} את המצב {% equation %}\left|0\right\rangle +e^{2\pi i0.j_{n-2}j_{n-1}j_{n}}\left|1\right\rangle {% endequation %}. הרעיון כבר ברור: נפעיל {% equation %}H{% endequation %} על {% equation %}\left|j_{n-2}\right\rangle {% endequation %} עצמו, ונפעיל {% equation %}S{% endequation %} מותנה על {% equation %}\left|j_{n-1}\right\rangle {% endequation %}, אבל עכשיו בשביל {% equation %}\left|j_{n}\right\rangle {% endequation %} צריך שער חדש - שער שהאפקט שלו הוא להשאיר את {% equation %}\left|0\right\rangle {% endequation %} ללא שינוי אבל לכפול את {% equation %}\left|1\right\rangle {% endequation %} ב-{% equation %}e^{2\pi i0.00j_{n}}{% endequation %}, כלומר במקרה שבו {% equation %}j_{n}=0{% endequation %} לא לעשות כלום (את זה משיגים בכך שהשער יהיה מותנה ב-{% equation %}\left|j_{n}\right\rangle {% endequation %}) ואם {% equation %}j_{n=1}{% endequation %} אז לכפול ב-{% equation %}e^{2\pi i0.001}=e^{\frac{2\pi i}{2^{3}}}{% endequation %}. אמנם, גם השער הזה חשוב מספיק כדי שיהיה לו שם משל עצמו (שער T, ועוד אדבר עליו בהמשך) אבל אנחנו מנסים להבין את הרעיון הכללי ולכן לא רוצים להמשיך להשתמש בשמות פרטניים לשערים. בשלב הזה כבר ברור שאנחנו צריכים לתת סימן כללי לשערים מהצורה {% equation %}e^{\frac{2\pi i}{2^{s}}}{% endequation %} עבור {% equation %}s\ge0{% endequation %}. הסימון המקובל הוא

{% equation %}R_{s}=\left(\begin{array}{cc} 1 & 0\\ 0 & e^{\frac{2\pi i}{2^{s}}} \end{array}\right){% endequation %}

אם כן, {% equation %}R_{1}=Z,R_{2}=S,R_{3}=T{% endequation %} ומשם והלאה אנחנו לא טורחים לתת להם שמות. אפשר לחשוב על זה גם ככה: {% equation %}R_{s+1}=\sqrt{R_{s}}{% endequation %} (כשיש לנו מטריצה אלכסונית, השורש שלה הוא המטריצה שהאיברים על האלכסון שלה הם השורש של האיברים על האלכסון במטריצה המקורית; אבל "שורש" במספרים מרוכבים הוא עניין מסובך יותר מזה ולכן זו אינטואיציה בלבד).

אם כן, מה שאנחנו עושים ל-{% equation %}\left|j_{n-2}\right\rangle {% endequation %} הוא שלושה דברים:

<ul> <li>מפעילים שער {% equation %}H{% endequation %} על {% equation %}\left|j_{n-2}\right\rangle {% endequation %} - זה מה שמייצר את הסופרפוזיציה הראשונית של {% equation %}\left|0\right\rangle {% endequation %} ו-{% equation %}\left|1\right\rangle {% endequation %} ועל הדרך גם כופל את {% equation %}\left|1\right\rangle {% endequation %} ב-{% equation %}-1{% endequation %} אם {% equation %}j_{n-2}=1{% endequation %} (שימו לב שאנחנו <strong>לא</strong> משתמשים פה ב-{% equation %}R_{1}=Z{% endequation %}).</li>


<li>מפעילים על {% equation %}\left|j_{n-2}\right\rangle {% endequation %} שער {% equation %}R_{2}{% endequation %} שמותנה ב-{% equation %}\left|j_{n-1}\right\rangle {% endequation %}.</li>


<li>מפעילים על {% equation %}\left|j_{n-2}\right\rangle {% endequation %} שער {% equation %}R_{3}{% endequation %} שמותנה ב-{% equation %}\left|j_{n}\right\rangle {% endequation %}</li>

</ul>

כל זה קורה <strong>לפני</strong> שאנחנו מטפלים בקיוביטים {% equation %}\left|j_{n-1}\right\rangle {% endequation %} ו-{% equation %}\left|j_{n}\right\rangle {% endequation %}.

אם {% equation %}n=3{% endequation %}, אחרי הטיפול ב-{% equation %}\left|j_{n-2}\right\rangle =\left|j_{1}\right\rangle {% endequation %} בעצם סיימנו את תיאור הפעולות שאנחנו מבצעים על כל הקיוביטים במעגל. רק צריך לזכור שבסוף המעגל עושים SWAP ל-{% equation %}\left|j_{1}\right\rangle {% endequation %} ול-{% equation %}\left|j_{3}\right\rangle {% endequation %}.

כך נראה המעגל במקרה הזה (האיקסים שמחוברים בקו בסיום מייצגים את ה-SWAP):

<img src="{{site.baseurl}}{{site.post_images}}/2022/QFT_3_qubits.png" alt=""/>

מכאן כבר די ברור מה צריך לקרות באופן כללי כשיש לנו {% equation %}n{% endequation %} קיוביטים. עבור הקיוביט ה-{% equation %}t{% endequation %}-י ({% equation %}1\le t\le n{% endequation %}), ראשית נפעיל עליו שער {% equation %}H{% endequation %} ולאחר מכן נפעיל עליו באופן סדרתי את השערים {% equation %}R_{2},R_{3},\ldots,R_{n+1-t}{% endequation %}, כאשר השער {% equation %}R_{k}{% endequation %} בסדרה הזו נשלט על ידי הקיוביט ה-{% equation %}k+t-1{% endequation %}. בסיום סדרת השערים הזו מתבצעים SWAP-ים: לכל {% equation %}1\le t\le n{% endequation %}, הקיוביט {% equation %}t{% endequation %} מוחלף עם הקיוביט {% equation %}n+1-t{% endequation %} (כשיש מספר אי זוגי של קיוביטים מן הסתם הקיוביט האמצעי לא יוחלף עם עצמו אלא פשוט לא נעשה לו כלום.

המעגל הזה פשוט עד להפתיע, ביחס לכל כאב הראש שעברנו עד אליו. הוא גם קטן: יש {% equation %}n{% endequation %} קיוביטים ועל כל אחד מהם מופעלים {% equation %}O\left(n\right){% endequation %} שערים, כך שבסך הכל המעגל דורש {% equation %}O\left(n^{2}\right)=O\left(\log^{2}N\right){% endequation %} שערים, כמו שהבטחתי בהתחלה.

הנה איך שזה נראה באופן כללי, רק בלי שערי ה-SWAP בסוף שקצת בעייתי לצייר:

<img src="{{site.baseurl}}{{site.post_images}}/2022/QFT_n_qubits.png" alt=""/>

מה עדיין חסר לנו? שימוש כלשהו שיראה למה כל זה היה טוב. שימוש מרהיב כזה יהיה בפוסט הבא; לרוע המזל, השימוש אמנם משתמש בפורייה בצורה מרהיבה אבל אחרי הפוסט הבא כנראה נשאל את עצמנו בשביל מה משתמשים בשימוש הזה. ואז יגיע האלגוריתם של שור. 