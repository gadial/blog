---
title: "סדרות וטורים של פונקציות"
layout: post
categories:
  - אנליזה מתמטית
tags:
  - סדרות של פונקציות
  - טורים של פונקציות
---


<h2>מבוא</h2>

חור גדול שנותר עד היום בבלוג הוא אותו חלק של החשבון הדיפרנציאלי והאינטגרלי שמתעסק <strong>בטורים של פונקציות</strong>. לא רק שזה נושא מגניב בפני עצמו, אלא גם שהמחסור בו הוא המכשול הגדול ביותר בדרך שלי לסגירת עוד חור גדול בבלוג - <strong>אנליזה מרוכבת</strong>. אז בואו נסגור את החור הזה סוף סוף.

אני אניח פה שאנחנו מכירים את מושגי הבסיס הרלוונטיים בחדו"א, כי יש לי כבר פוסטים עליהם: <a href="https://gadial.net/2010/10/26/limit_of_functions_and_continuity/">על המושגים של גבול של פונקציה ופונקציות רציפות</a>; על <a href="https://gadial.net/2010/10/03/limit_of_sequence/">גבולות של סדרות</a>; <a href="https://gadial.net/2008/06/17/infinite_series/">ועל טורים אינסופיים של מספרים</a>. אבל אין סיבה עקרונית לא להזכיר את המושגים הללו בקיצור גם כאן, כי נשתמש בהם כל הזמן.

אנחנו בחדו"א עובדים מעל {% equation %}\mathbb{R}{% endequation %}, כלומר מתעסקים בסדרות שהאיברים שלהן הם מספרים ממשיים ופונקציות שמקבלות ממשיים ומחזירות ממשיים. על הממשיים מוגדר לנו מושג של <strong>מרחק</strong> בעזרת פונקציית הערך המוחלט: המרחק בין {% equation %}a{% endequation %} ל-{% equation %}b{% endequation %} הוא {% equation %}\left|a-b\right|{% endequation %}. הרעיון הכללי מאחורי <strong>גבול</strong>, המושג שעליו החדו"א המודרני נבנה, הוא שהאובייקט שלנו (סדרה או פונקציה) "מתקרב" אל ערך אחד ספציפי - הגבול - במובן זה שהמרחק ביניהם נהיה "קטן כרצוננו" אם מתמקדים בחלק של האובייקט שלנו שעליו אומרים שהוא שואף אל הגבול. בואו נראה איך זה בא לידי ביטוי בסדרות של מספרים ובפונקציות:

<ul> <li>אומרים שהסדרה האינסופית {% equation %}\left\{ a_{n}\right\} _{n=0}^{\infty}{% endequation %} <strong>שואפת</strong> לגבול {% equation %}L{% endequation %} ומסמנים את זה {% equation %}\lim_{n\to\infty}a_{n}=L{% endequation %} (או סתם {% equation %}a_{n}\to L{% endequation %}) אם <strong>לכל</strong> {% equation %}\varepsilon>0{% endequation %} <strong>קיים</strong> {% equation %}N{% endequation %} טבעי כך שלכל {% equation %}n>N{% endequation %} מתקיים {% equation %}\left|a_{n}-L\right|<\varepsilon{% endequation %}</li>


<li>אומרים שהפונקציה {% equation %}f\left(x\right):\mathbb{R\to\mathbb{R}}{% endequation %} <strong>שואפת לגבול</strong> {% equation %}L{% endequation %} כאשר {% equation %}x{% endequation %} <strong>שואף</strong> לנקודה {% equation %}x_{0}{% endequation %} ומסמנים את זה {% equation %}\lim_{x\to x_{0}}f\left(x\right)=L{% endequation %} אם <strong>לכל</strong> {% equation %}\varepsilon>0{% endequation %} <strong>קיים</strong> {% equation %}\delta>0{% endequation %} כך שאם {% equation %}0<\left|x-x_{0}\right|<\delta{% endequation %} אז {% equation %}\left|f\left(x\right)-L\right|<\varepsilon{% endequation %}</li>

</ul>

זו לא הגדרה קלה לעיכול ולכן אני ממליץ על הפוסטים שקישרתי אליהם (או המקורות הרבים האחרים שמסבירים את הנושא טוב ממני!) אם היא לא יושבת טוב כרגע. אני רוצה שננצל את ההזדמנות לכך ששתי הההגדרות יושבות זו לצד זו כדי לראות את הדמיון הרב ביניהן: בהגדרה הראשונה אנחנו מסתכלים על החלק של הסדרה שהוא "כל מה שגדול מ-{% equation %}N{% endequation %}" ובהגדרה השניה אנחנו מסתכלים על החלק של הפונקציה שהוא "כל הפלטים של הפונקציה על סביבה בגודל {% equation %}\delta{% endequation %} של {% equation %}x_{0}{% endequation %} שלא כוללת את הקצוות או את {% equation %}x_{0}{% endequation %} עצמה" ובשני המקרים אנחנו דורשים ש<strong>כל</strong> מה שנמצא באותו איזור שאנחנו מסתכלים עליו יהיה קרוב ל-{% equation %}L{% endequation %} עד כדי ה-{% equation %}\varepsilon{% endequation %} השרירותי שהתחלנו ממנו.

ההגדרה של <strong>רציפות</strong> של פונקציה היא נקודתית - כלומר אומרים שפונקציה היא רציפה בנקודה ספציפית. כדי ש-{% equation %}f{% endequation %} תהיה רציפה ב-{% equation %}x_{0}{% endequation %} היא צריכה לקיים {% equation %}f\left(x_{0}\right)=\lim_{x\to x_{0}}f\left(x\right){% endequation %}, כלומר שהפונקציה "תקיים את ההבטחה" של הגבול. אפשר גם להגדיר את זה ישירות: קיים {% equation %}L{% endequation %} כך שלכל {% equation %}\varepsilon>0{% endequation %} קיים {% equation %}\delta>0{% endequation %} כך שאם {% equation %}\left|x-x_{0}\right|<\delta{% endequation %} אז {% equation %}\left|f\left(x\right)-L\right|<\varepsilon{% endequation %} (שימו לב שבעורמה רבה הסרתי את הדרישה המקילה {% equation %}0<\left|x-x_{0}\right|{% endequation %} ובכך אני מכריח את השוויון {% equation %}f\left(x_{0}\right)=L{% endequation %} להתקיים).

לבסוף, ההגדרה של <strong>סכום של טור אינסופי</strong> של מספרים בעצם נבנית מעל ההגדרה של גבול של סדרה. הרעיון הוא כזה: יש לנו סדרה {% equation %}a_{0},a_{1},a_{2},\ldots{% endequation %} ואנחנו רוצים לחבר את האיברים שלה - להסתכל על {% equation %}\sum_{n=0}^{\infty}a_{n}{% endequation %} ולמצוא מספר שמתאים לאינטואיציה שלנו לגבי הסכום של אותם אינסוף מספרים. יש כמה גישות לנושא הזה - אין הגדרה אחת שהיא פשוט "ההגדרה הנכונה" אבל זו השימושית והנפוצה ביותר במתמטיקה משתמשת במשהו שנקרא <strong>סכומים חלקיים</strong> ומגדירה את סכום הטור בתור הגבול של הסכומים החלקיים הללו. פורמלית, אני מגדיר {% equation %}S_{n}=\sum_{k=0}^{n}a_{k}{% endequation %} ואז אומר ש-{% equation %}\sum_{n=0}^{\infty}a_{n}=S{% endequation %} אם {% equation %}\lim_{n\to\infty}S_{n}=S{% endequation %}.

אם קיים גבול לסדרת הסכומים החלקיים אומרים שהטור {% equation %}\sum_{n=0}^{\infty}a_{n}{% endequation %} <strong>מתכנס</strong> ואחרת אומרים שהוא <strong>מתבדר</strong>. יש גם מושג של "התכנסות לאינסוף" אבל נעזוב את זה; תחשבו על זה בתור אחד מסוגי ההתבדרות. סוג אחר של התבדרות הוא של הטור {% equation %}1-1+1-1+1-\ldots{% endequation %} שהסכומים החלקיים שלו "מזפזפים" בין 0 ו-1; על פי ההגדרה שלנו אין לטור הזה סכום (על פי הגדרה אחרת, כללית יותר, שלוקחת את הגבול של <strong>הממוצע</strong> של סדרת הסכומים החלקיים, דווקא יש גבול והוא {% equation %}\frac{1}{2}{% endequation %}).

בואו נראה שאנחנו מבינים מספיק מה הולך פה כדי להוכיח משהו! טענה בסיסית אבל מועילה מאוד - שאם {% equation %}\sum_{n=0}^{\infty}a_{n}{% endequation %} מתכנס אז האיבר הכללי של הטור שואף לאפס, כלומר {% equation %}\lim_{n\to\infty}a_{n}=0{% endequation %} (שימו לב - זו לא סדרת הסכומים החלקיים!)

איך מוכיחים טענה כזו? כלל האצבע שלי לכל מי שנתקעים בהוכחות בחדו"א - קודם כל תתחילו מ"יהא {% equation %}\varepsilon>0{% endequation %}". זה בדרך כלל עובד. ה-{% equation %}\varepsilon{% endequation %} מציב בפנינו "אתגר" - הוא אומר לנו - עכשיו בואו תמצאו {% equation %}N{% endequation %} כלשהו כך שאם {% equation %}n>N{% endequation %} אז {% equation %}\left|a_{n}-0\right|<\varepsilon{% endequation %}, דהיינו פשוט {% equation %}\left|a_{n}\right|<\varepsilon{% endequation %}.

הרעיון הוא פשוט. מה <strong>נתון</strong> לנו? ש-{% equation %}\sum_{n=0}^{\infty}a_{n}{% endequation %} <strong>מתכנס</strong>, כלומר קיים {% equation %}L{% endequation %} כך ש-{% equation %}\lim_{n\to\infty}S_{n}=L{% endequation %}. אם הנתון שלנו הוא על הסכומים החלקיים {% equation %}S_{n}{% endequation %} ואנחנו רוצים לומר משהו על האיברים {% equation %}a_{n}{% endequation %}, מה הקשר ביניהם? הוא פשוט: {% equation %}a_{n}=S_{n}-S_{n-1}{% endequation %}. לכן אפשר לנקוט בתעלול הבא, שהוא מאוד נפוצות בהוכחות חדו"א: מכך ש-{% equation %}S_{n}{% endequation %} מתכנסת אל {% equation %}L{% endequation %} נובע שקיים {% equation %}N^{\prime}{% endequation %} כך שאם {% equation %}n>N^{\prime}{% endequation %} אז {% equation %}\left|S_{n}-L\right|<\frac{\varepsilon}{2}{% endequation %} (כלומר - באנו אל הטענה ש-{% equation %}S_{n}{% endequation %} מתכנסת אל {% equation %}L{% endequation %} ונתנו לה "אתגר" משלנו, עם {% equation %}\frac{\varepsilon}{2}{% endequation %}; היא ענתה לנו עם התשובה {% equation %}N^{\prime}{% endequation %}). עכשיו נגדיר {% equation %}N=N^{\prime}+1{% endequation %}. מה יצא לנו מזה? ניקח {% equation %}n>N{% endequation %}; זה אומר ש-{% equation %}n>N^{\prime}{% endequation %} <strong>ובנוסף לכך</strong> גם {% equation %}n-1>N^{\prime}{% endequation %}, ולכן אנחנו מקבלים גם {% equation %}\left|S_{n}-L\right|<\frac{\varepsilon}{2}{% endequation %} וגם {% equation %}\left|S_{n-1}-L\right|<\frac{\varepsilon}{2}{% endequation %}. וכעת הנה הקסם:

{% equation %}\left|a_{n}\right|=\left|S_{n}-S_{n-1}\right|=\left|\left(S_{n}-L\right)-\left(S_{n-1}-L\right)\right|\le{% endequation %}

{% equation %}\le\left|S_{n}-L\right|+\left|S_{n-1}-L\right|<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon{% endequation %}

עמדנו ביעד המקורי שלנו! שימו לב לטריקים שעשינו בהתחלה - הוספנו וחיסרנו {% equation %}L{% endequation %} לביטוי שבתוך הערך המוחלט, והשתמשנו באי-שוויון המשולש כדי לפרק את הביטוי המסובך שבתוך הערך המוחלט לשני ביטויים שונים בערכים מוחלטים שתואמים בדיוק את מה שהיה נתון לנו. כאמור, הכל די סטנדרטי בחדו"א ואני אניח שאנחנו בסדר עם זה כי אני הולך לעשות את זה גם בהמשך.

<h2>סדרות של פונקציות</h2>

דיברנו על סדרות, ודיברנו על פונקציות. למה שלא נשלב את שני אלו? במקום לדבר על סדרה {% equation %}a_{0},a_{1},a_{2},\ldots{% endequation %} של <strong>מספרים</strong> (איברים של {% equation %}\mathbb{R}{% endequation %}) אפשר לדבר על סדרה {% equation %}f_{0}\left(x\right),f_{1}\left(x\right),f_{2}\left(x\right),\ldots{% endequation %} של <strong>פונקציות</strong>, {% equation %}f_{n}\left(x\right):D\to\mathbb{R}{% endequation %} שהתחום שלהן הוא תת-קבוצה כלשהי {% equation %}D\subseteq\mathbb{R}{% endequation %} והטווח שלהן הוא {% equation %}\mathbb{R}{% endequation %}. עכשיו, אם יש לנו סדרה של פונקציות, אפשר לדבר על התכנסות שלה. עכשיו, כמו שסדרה של מספרים מתכנסת למספר, סדרה של פונקציות תתכנס לפונקציה {% equation %}f:D\to\mathbb{R}{% endequation %}.

אם ננסה לקחת את ההגדרה הרגילה של גבול של סדרה ולהשתמש בה פה, נקבל משהו כזה: נאמר שהסדרה {% equation %}\left\{ f_{n}\right\} _{n=0}^{\infty}{% endequation %} מתכנסת אל {% equation %}f{% endequation %} אם לכל {% equation %}\varepsilon>0{% endequation %} קיים {% equation %}N{% endequation %} כך שלכל {% equation %}n>N{% endequation %} מתקיים {% equation %}\left|f-f_{n}\right|<\varepsilon{% endequation %}. נשמע הגיוני? ובכן, זה אכן הגיוני אבל יש כאן משהו שלא הוגדר עד הסוף - ואם הולכים איתו עד הסוף מקבלים בעצם שלוש גישות שונות להגדרת גבול שכזה.

מה שלא ברור עד הסוף הוא מה הכוונה שלי בביטוי {% equation %}\left|f-f_{n}\right|<\varepsilon{% endequation %}. הרי הסימן {% equation %}\left|\cdot\right|{% endequation %} (שני קווים אנכיים עם משהו בפנים) בא לתאר <strong>ערך מוחלט</strong>, שהוא משהו שמוגדר על מספרים, לא על פונקציות. קונספטואלית מה שאני רוצה פה הוא לדבר על <strong>המרחק</strong> בין {% equation %}f{% endequation %} ובין {% equation %}f_{n}{% endequation %} - כלומר להכניס לתמונה פונקצית מרחק חדשה, שונה מהערך המוחלט של מספרים ממשיים. יש תורה שלמה שעוסקת בדברים הללו; מה שבדרך כלל עושים הוא להגדיר <strong>נורמה</strong>, שהיא פונקציה שלוקחת איבר ומחזירה הערכה ל"גודל" שלו, ואז מגדירים מרחק על ידי הנורמה של ההפרש: {% equation %}\|f_{n}-f\|{% endequation %}. יש כל מני דרכים להגדיר נורמות של פונקציות וזה מוביל אותנו לתחום מרתק שנקרא <strong>אנליזה פונקציונלית</strong> ואני בשום פנים ואופן לא הולך לומר על כל זה שום דבר הפעם. זו פשוט לא ההגדרה שבה נתעסק.

הגישה האחרת שבה אפשר לנקוט היא להמשיך להשתמש בערך המוחלט "הרגיל", על ידי כך שאנחנו משווים את הערכים ש-{% equation %}f_{n},f{% endequation %} מחזירות. אלא שכאן אנחנו מתפצלים לשתי הגדרות שונות בהתאם לדקות הניסוח שלנו, ואני אציג את שתי ההגדרות בבת אחת כדי שיהיה קל לראות את הדקות הזו:

<ul> <li>נאמר ש-{% equation %}f_{n}{% endequation %} <strong>מתכנסת</strong> ("נקודתית") אל {% equation %}f{% endequation %} אם לכל {% equation %}x\in D{% endequation %}, לכל {% equation %}\varepsilon>0{% endequation %} קיים {% equation %}N{% endequation %} כך שאם {% equation %}n>N{% endequation %} אז {% equation %}\left|f_{n}\left(x\right)-f\left(x\right)\right|<\varepsilon{% endequation %}</li>


<li>נאמר ש-{% equation %}f_{n}{% endequation %} <strong>מתכנסת במידה שווה</strong> (במ"ש) אל {% equation %}f{% endequation %} אם לכל {% equation %}\varepsilon>0{% endequation %} קיים {% equation %}N{% endequation %} כך שאם {% equation %}n>N{% endequation %} אז {% equation %}\left|f_{n}\left(x\right)-f\left(x\right)\right|<\varepsilon{% endequation %} לכל {% equation %}x\in D{% endequation %}</li>

</ul>

מה ההבדל בין ההגדרות? המיקום של ה"לכל {% equation %}x{% endequation %}". צריך לחשוב על זה ככה: במקרה הראשון, כשנותנים לנו את האתגר של {% equation %}\varepsilon{% endequation %} ואנחנו צריכים למצוא {% equation %}N{% endequation %} עבורו, ה-{% equation %}N{% endequation %} הזה צריך לעבוד רק עבור הערכים של הפונקציות ב-{% equation %}x{% endequation %}. זה בעצם אומר שלכל {% equation %}x\in D{% endequation %}, צריך להתקיים {% equation %}f\left(x\right)=\lim_{n\to\infty}f_{n}\left(x\right){% endequation %} כאשר כאן מה שיש לנו בגבול הוא סדרה של <strong>מספרים</strong> - הערכים שמקבלים כשמציבים את {% equation %}x{% endequation %} בכל הפונקציות {% equation %}f_{n}{% endequation %}. לעומת זאת, במקרה השני באתגר של ה-{% equation %}\varepsilon{% endequation %} אנחנו צריכים למצוא {% equation %}N{% endequation %} שעובד עבור <strong>כל הערכים האפשריים</strong> של {% equation %}x{% endequation %} בו זמנית. זה אתגר יותר גדול, ובאמת יש סיטואציות של סדרת פונקציות שמתכנסת אבל לא מתכנסת במידה שווה. בואו נראה דוגמא כזו - למרבה השמחה יש אחת פשוטה מאוד.

התחום שלנו יהיה {% equation %}D=\left[0,1\right]{% endequation %} וסדרת הפונקציות תהיה {% equation %}f_{n}\left(x\right)=x^{n}{% endequation %}. עכשיו, אנחנו יודעים מחדו"א בסיסי שאם {% equation %}0\le x<1{% endequation %} אז {% equation %}x^{n}\to0{% endequation %}, אבל כמובן ש-{% equation %}1^{n}\to1{% endequation %}. כלומר, אם נגדיר {% equation %}f\left(x\right)=\lim_{n\to\infty}f_{n}\left(x\right){% endequation %} נקבל את הפונקציה

{% equation %}f\left(x\right)=\begin{cases} 0 & x\ne1\\ 1 & x=1 \end{cases}{% endequation %}

האם {% equation %}f_{n}{% endequation %} מתכנסת במידה שווה אל {% equation %}f{% endequation %}? הנה טיעון טכני שמראה מה הבעיה, עם מספרים מהונדסים של מישהו שכבר יודע מה הוא מנסה להשיג וכל הכיף הרגיל של חדו"א: כדי להראות שאין התכנסות במ"ש אני אקח למשל {% equation %}\varepsilon=\frac{1}{e}{% endequation %}. ועכשיו נסתכל על {% equation %}N{% endequation %} כלשהו ונראה שאפילו אם {% equation %}n>N{% endequation %} אז עדיין לא <strong>לכל</strong> {% equation %}x\in D{% endequation %} יתקיים {% equation %}\left|f_{n}\left(x\right)-f\left(x\right)\right|<\frac{1}{e}{% endequation %}. איך נראה את זה? אם {% equation %}x<1{% endequation %} אז {% equation %}\left|f_{n}\left(x\right)-f\left(x\right)\right|=\left|x^{n}-0\right|=\left|x^{n}\right|=x^{n}{% endequation %}. עכשיו, אין לנו שליטה על {% equation %}n{% endequation %} אבל את {% equation %}x{% endequation %} אנחנו יכולים להגדיל כרצוננו אל {% equation %}1{% endequation %} עד שנעבור את {% equation %}\frac{1}{e}{% endequation %}. הנה האופן שבו אפשר למצוא {% equation %}x{% endequation %} מתאים שכזה - בעזרת <strong>לוגריתמים</strong>. אני אחפש {% equation %}x{% endequation %} שמקיים {% equation %}x^{n}=\frac{1}{e}{% endequation %}, כלומר {% equation %}\ln\left(x^{n}\right)=\ln\left(e^{-1}\right){% endequation %}, כלומר {% equation %}n\ln x=-1\ln e=-1{% endequation %}, כלומר {% equation %}\ln x=-\frac{1}{n}{% endequation %}. למרבה השמחה אני יודע ש-{% equation %}\ln x{% endequation %} היא פונקציה מונוטונית עולה שמקיימת {% equation %}\lim_{x\to0}\ln x=-\infty{% endequation %} ו-{% equation %}\ln1=0{% endequation %} ולכן קיים {% equation %}x\in D{% endequation %} כך ש-{% equation %}\ln x=-\frac{1}{n}{% endequation %}, וה-{% equation %}x{% endequation %} הזה שובר את הטענה על התכנסות במ"ש.

<h2>איך התכנסות במ"ש משמרת רציפות</h2>

הטיעון למעלה היה טכני למדי, אבל מה שנחמד הוא שאני <strong>לא באמת צריך אותו</strong> כי אפשר לראות ש-{% equation %}f_{n}{% endequation %} לא מתכנסת במ"ש בקלות מתוך טענה כללית יותר ושימושית מאוד, שגם עוזרת לנו להבין מה הטעם בהגדרה הזו של התכנסות במ"ש. הטענה היא שאם <strong>כל</strong> {% equation %}f_{n}{% endequation %} היא פונקציה רציפה ו-{% equation %}f_{n}\to f{% endequation %} וההתכנסות היא במ"ש, אז גם {% equation %}f{% endequation %} רציפה. זו דוגמא לסוג הטענות שמעניינות אותנו בכללי - אנחנו רוצים לומר משהו חכם על {% equation %}f{% endequation %} אבל זה קשה לנו, אז אנחנו מוצאים סדרה פשוטה יחסית שמתכנסת אל {% equation %}f{% endequation %} ועל האיברים שלה קל לנו יותר לומר משהו חכם, ואז מקווים ממש חזק שהמשהו החכם הזה יעבור מהסדרה אל {% equation %}f{% endequation %} עצמה. במקרה שבו המשהו החכם הוא "רציפות" וההתכנסות היא במ"ש, זה גם עובד.

עבור הדוגמא שנתתי למעלה, {% equation %}f_{n}\left(x\right)=x^{n}{% endequation %} היא בוודאי פונקציה רציפה, אבל {% equation %}f\left(x\right){% endequation %} שאליה הסדרה מתכנסת היא לא רציפה - היא 0 בכל מקום חוץ מ-{% equation %}x=1{% endequation %} ושם היא קופצת אל {% equation %}1{% endequation %} - זו נקודת אי רציפות. לכן פשוט לא ייתכן שההתכנסות תהיה במ"ש; הרבה יותר פשוט מאשר להתחיל לערב בתמונה לוגריתמים וכדומה. בפועל? אנחנו מטאטאים את הסיבוך מתחת לשטיח עם הסתמכות על היכולת שלי לומר בקלילות ש-{% equation %}x^{n}{% endequation %} "היא בוודאי פונקציה רציפה" - אם ננסה להוכיח את <strong>זה</strong> במפורש שוב נצטרך עבודה טכנית - אבל זה כל היופי, לבנות על הידע הטכני שכבר יש לנו ועל משפטים אבסטרקטיים כדי לקבל תוצאות טכניות חדשות בלי מאמץ טכני נוסף.

בואו נוכיח את הטענה: נתון לי ש-{% equation %}\left\{ f_{n}\right\} _{n=0}^{\infty}{% endequation %} היא סדרה של פונקציות רציפות וש-{% equation %}f_{n}\to f{% endequation %} בהתכנסות במ"ש, ואני צריך להוכיח ש-{% equation %}f{% endequation %} רציפה. איך מוכיחים שמשהו הוא רציף? מתחילים כרגיל עם "יהא {% equation %}\varepsilon>0{% endequation %}" יחד עם נקודה ספציפית {% equation %}x_{0}\in D{% endequation %}. האתגר שלנו הוא למצוא {% equation %}\delta{% endequation %} כך שלכל {% equation %}x\in D{% endequation %} המקיים {% equation %}\left|x-x_{0}\right|<\delta{% endequation %} מתקיים {% equation %}\left|f\left(x\right)-f\left(x_{0}\right)\right|<\varepsilon{% endequation %}. הנה האסטרטגיה שלנו: אנחנו נמצא פונקציה {% equation %}f_{n}{% endequation %} שקרובה מספיק אל {% equation %}f{% endequation %}, ואז נשתמש בכך שהיא רציפה כדי לחסום את המרחק בין {% equation %}f_{n}\left(x\right),f_{n}\left(x_{0}\right){% endequation %} ונבנה על כך שהמרחקים של {% equation %}f_{n}{% endequation %} בנקודות הללו מהנקודות המקבילות אצל {% equation %}f{% endequation %} הם קטנים. כלומר, אנחנו צריכים ששלושה דברים יהיו קטנים:

<ul> <li>{% equation %}\left|f_{n}\left(x\right)-f_{n}\left(x_{0}\right)\right|{% endequation %}</li>


<li>{% equation %}\left|f_{n}\left(x\right)-f\left(x\right)\right|{% endequation %}</li>


<li>{% equation %}\left|f_{n}\left(x_{0}\right)-f\left(x_{0}\right)\right|{% endequation %}</li>

</ul>

מכיוון שיש לנו שלושה דברים שכפי שנראה בסוף איכשהו הכל יתבטא בסכום שלהם, שווה לנו לעבוד עם {% equation %}\frac{\varepsilon}{3}{% endequation %}. פורמלית, ניעזר בכך שההתכנסות {% equation %}f_{n}\to f{% endequation %} היא במידה שווה, ונמצא {% equation %}N{% endequation %} כך שלכל {% equation %}n>N{% endequation %} <strong>ולכל</strong> {% equation %}x\in D{% endequation %} מתקיים {% equation %}\left|f_{n}\left(x\right)-f\left(x\right)\right|<\frac{\varepsilon}{3}{% endequation %}. שימו לב שזה קריטי שזה יתקיים <strong>לכל</strong> {% equation %}x{% endequation %} כי כרגע אין לנו בכלל ערך קונקרטי אחד של {% equation %}x{% endequation %} שאנחנו רוצים לטפל בו - אנחנו נרצה לטפל <strong>בכל</strong> {% equation %}x{% endequation %} שיהיה קרוב אל {% equation %}x_{0}{% endequation %} עד כדי {% equation %}\delta{% endequation %} (וה-{% equation %}\delta{% endequation %} אפילו לא ידוע בשלב הזה). כלומר, בלי התכנסות במ"ש אין לי אפילו מאיפה להתחיל.

יופי, אז יש לנו {% equation %}n{% endequation %} שעבורו {% equation %}\left|f_{n}\left(x\right)-f\left(x\right)\right|<\frac{\varepsilon}{3}{% endequation %} לכל {% equation %}x\in D{% endequation %}. עכשיו נשתמש בכך ש-{% equation %}f_{n}{% endequation %} רציפה בכל {% equation %}D{% endequation %} ובפרט ב-{% equation %}x_{0}\in D{% endequation %} כדי למצוא {% equation %}\delta{% endequation %} בעל התכונה שאם {% equation %}\left|x-x_{0}\right|<\delta{% endequation %} אז {% equation %}\left|f_{n}\left(x\right)-f_{n}\left(x_{0}\right)\right|<\frac{\varepsilon}{3}{% endequation %}. כלומר - השתמשנו בתכונת הרציפות תוך שה"אתגר" ש<strong>אנחנו</strong> מציבים הוא עם {% equation %}\frac{\varepsilon}{3}{% endequation %} (זו נקודה מבלבלת: כשאנחנו מוכיחים שרציפות מתקיימת, אנחנו <strong>מקבלים</strong> את האתגר <strong>ומחפשים</strong> {% equation %}\delta{% endequation %} מתאים; כשאנחנו <strong>משתמשים</strong> ברציפות אנחנו <strong>נותנים</strong> את האתגר ו<strong>מקבלים</strong> {% equation %}\delta{% endequation %} מתאים).

עכשיו, יהא {% equation %}x\in D{% endequation %} כלשהו שעבורו באמת מתקיים {% equation %}\left|x-x_{0}\right|<\delta{% endequation %}. אנחנו צריכים להוכיח {% equation %}\left|f\left(x\right)-f\left(x_{0}\right)\right|<\varepsilon{% endequation %} ואת זה נעשה על ידי טכניקה סטנדרטית של חיבור/חיסור אותו איבר ואז פירוק הערך המוחלט לסכום של ערכים מוחלטים תוך שימוש באי-שוויון המשולש: טכניקות סטנדרטיות בחדו"א שלכל הפחות אני כבר מכיר מספיק טוב כדי ליהנות מהם ואני מקווה שזה המצב לא רק אצלי:

{% equation %}\left|f\left(x\right)-f\left(x_{0}\right)\right|=\left|f\left(x\right)-\left(f_{n}\left(x\right)-f_{n}\left(x\right)\right)-\left(f_{n}\left(x_{0}\right)-f_{n}\left(x_{0}\right)\right)-f\left(x_{0}\right)\right|{% endequation %}

{% equation %}=\left|\left(f\left(x\right)-f_{n}\left(x\right)\right)+\left(f_{n}\left(x\right)-f_{n}\left(x_{0}\right)\right)+\left(f_{n}\left(x_{0}\right)-f\left(x_{0}\right)\right)\right|{% endequation %}

{% equation %}\le\left|f\left(x\right)-f_{n}\left(x\right)\right|+\left|f_{n}\left(x\right)-f_{n}\left(x_{0}\right)\right|+\left|f_{n}\left(x_{0}\right)-f\left(x_{0}\right)\right|{% endequation %}

{% equation %}\le\frac{\varepsilon}{3}+\frac{\varepsilon}{3}+\frac{\varepsilon}{3}=\varepsilon{% endequation %}

מה שמסיים את ההוכחה הזו.

<h2>עד כמה התכנסות במ"ש משמרת אינטגרלים ונגזרות?</h2>

שני המושגים המרכזיים שהחדו"א עוסק בהם הם <a href="https://gadial.net/2010/11/27/integral/">אינטגרלים</a> (ספציפית, אינטגרל רימן) <a href="https://gadial.net/2010/11/21/derivative/">ונגזרות</a>. על שניהם יש לי פוסטים כך שלא אגדיר אותם במפורש כאן אלא אשתמש רק במה שאני צריך. השאלה הבסיסית שלנו היא זו: נניח ש-{% equation %}f_{n}\to f{% endequation %}, האם זה אומר ש-{% equation %}\int_{a}^{b}f_{n}\to\int_{a}^{b}f{% endequation %} עבור {% equation %}\left[a,b\right]\subseteq D{% endequation %}? והאם זה אומר ש-{% equation %}f_{n}^{\prime}\to f^{\prime}{% endequation %}? התשובה היא שהתכנסות במ"ש מבטיחה את המשפט לגבי האינטגרל, אבל לגבי הנגזרות... זה מסובך קצת יותר. אז בואו נתחיל עם האינטגרל.

ובכן, אני מניח ש-{% equation %}f_{n}\to f{% endequation %} במ"ש ואני רוצה להוכיח {% equation %}\int_{a}^{b}f_{n}\to\int_{a}^{b}f{% endequation %}. איך מתחילים הוכחה כזו? האם הולכים להגדרת אינטגרל רימן, נאמר בעזרת הזוועה שנקראת "סכומי דארבו" ומתחילים לפרק את {% equation %}\left[a,b\right]{% endequation %} לכל מני תת-חלוקות? לא... אנחנו בחדו"א, חבר'ה! מתחילים הכל כולל הכל קודם כל ב"יהי {% equation %}\varepsilon>0{% endequation %}" ואז כבר רואים איך להתקדם מזה! מה שאנחנו רוצים הוא להראות {% equation %}\int_{a}^{b}f_{n}\to\int_{a}^{b}f{% endequation %}, וזו התכנסות של סדרת מספרים; כלומר, לכל {% equation %}\varepsilon>0{% endequation %} אני צריך למצוא {% equation %}N{% endequation %} כך שאם {% equation %}n>N{% endequation %} אז {% equation %}\left|\int_{a}^{b}f\left(x\right)dx-\int_{a}^{b}f_{n}\left(x\right)dx\right|<\varepsilon{% endequation %}. בשביל להראות את זה אנחנו לא צריכים להיכנס לסכומי דארבו אבל כן צריכים כמה תכונות סטנדרטיות של אינטגרלים:

<ul> <li>לינאריות של אינטגרל: {% equation %}\int_{a}^{b}f\left(x\right)dx+\int_{a}^{b}g\left(x\right)dx=\int_{a}^{b}\left[f\left(x\right)+g\left(x\right)\right]dx{% endequation %}</li>


<li>אי שוויון המשולש האינטגרלי: {% equation %}\left|\int_{a}^{b}f\left(x\right)dx\right|\le\int_{a}^{b}\left|f\left(x\right)\right|dx{% endequation %}</li>


<li>מונוטוניות של אינטגרל: אם {% equation %}f\left(x\right)\le g\left(x\right){% endequation %} ב-{% equation %}\left[a,b\right]{% endequation %} אז {% equation %}\int_{a}^{b}f\left(x\right)dx\le\int_{a}^{b}g\left(x\right)dx{% endequation %}</li>


<li>אינטגרל של קבוע: {% equation %}\int_{a}^{b}Adx=\left(b-a\right)\cdot A{% endequation %}</li>

</ul>

יחד עם אלו, קל להתקדם: מכיוון ש-{% equation %}f_{n}\to f{% endequation %} במ"ש, אז עבור {% equation %}\frac{\varepsilon}{b-a}>0{% endequation %} נמצא {% equation %}N{% endequation %} כך שלכל {% equation %}n>N{% endequation %} מתקיים {% equation %}\left|f_{n}\left(x\right)-f\left(x\right)\right|<\frac{\varepsilon}{b-a}{% endequation %} לכל {% equation %}x\in D{% endequation %} ובפרט לכל {% equation %}a\le x\le b{% endequation %} (למה דווקא {% equation %}\frac{\varepsilon}{b-a}{% endequation %}? אני מניח שאנחנו רגילים בשלב הזה לכך שאפשר קודם לנסות עבור {% equation %}\varepsilon^{\prime}{% endequation %} כללי, לראות מה הערך שיוצא לנו טוב ואז לתקן רטרואקטיבית). עכשיו, בעזרת התכונות שציטטתי:

{% equation %}\left|\int_{a}^{b}f\left(x\right)dx-\int_{a}^{b}f_{n}\left(x\right)dx\right|=\left|\int_{a}^{b}\left[f\left(x\right)-f_{n}\left(x\right)\right]dx\right|\le{% endequation %}

{% equation %}\le\int_{a}^{b}\left|f\left(x\right)-f_{n}\left(x\right)\right|dx\le\int_{a}^{b}\frac{\varepsilon}{b-a}=\left(b-a\right)\frac{\varepsilon}{b-a}=\varepsilon{% endequation %}

מה שמסיים את ההוכחה עבור אינטגרלים (ליתר דיוק, עבור מה שנקרא "אינטגרל רימן"; אני לא אדבר על סוגים אחרים בפוסט הזה).

בואו נעבור לנגזרות. <strong>מה שהיינו רוצים שיקרה</strong> הוא שאם {% equation %}f_{n}\to f{% endequation %} מתכנסת במ"ש, אז {% equation %}f_{n}^{\prime}\to f^{\prime}{% endequation %} (התכנסות נקודתית). הבעיה היא שזה לא קורה. אני אתן דוגמא עוד מעט. זה קצת מתסכל, כי הרי יש לנו משפט דומה על אינטגרלים ונגזרת היא סוג של ההפך מאינטגרל, כפי <a href="https://gadial.net/2011/01/02/fundemental_theorem_of_calculus/">שהמשפט היסודי של החדו“א</a> מראה לנו, אבל זה בעצם העניין - מכיון שנגזרת היא "ההפך מאינטגרל", אז כדי שהתוצאה החדשה תתאים למה שראינו על אינטגרלים צריך לא שהסדרה {% equation %}f_{n}\to f{% endequation %} תתכנס במ"ש אלא שהסדרה {% equation %}f_{n}^{\prime}\to f^{\prime}{% endequation %} תתכנס במ"ש.

בואו נחדד מה המשפט שאנחנו כן יודעים להוכיח: נניח ש-{% equation %}\left\{ f_{n}\right\} _{n=0}^{\infty}{% endequation %} היא סדרת פונקציות גזירות על {% equation %}\left[a,b\right]{% endequation %}, ונניח גם שהנגזרות שלהם {% equation %}f_{n}^{\prime}{% endequation %} הן אינטגרביליות על {% equation %}\left[a,b\right]{% endequation %}, ובנוסף לכך נניח ש-{% equation %}f_{n}\to f{% endequation %} בהתכנסות <strong>נקודתית</strong> (לא צריך התכנסות במ"ש). עכשיו, בואו נניח ש-{% equation %}f_{n}^{\prime}\to g{% endequation %} עבור {% equation %}g{% endequation %} <strong>רציפה </strong>כלשהי בהתכנסות שהיא <strong>כן במ"ש</strong>, אז מה שאני יכול לומר הוא ש-{% equation %}f{% endequation %} גזירה ו-{% equation %}f^{\prime}\left(x\right)=g{% endequation %}. אלו תנאים מסובכים למדי, אבל כשהם מתקיימים, המשפט הזה יכול להיות שימושי מאוד (כי בהחלט ייתכן שקל לנו לגזור את {% equation %}f_{n}{% endequation %} ולהראות בקלות שהנגזרות מתכנסות במ"ש למשהו רציף, אפילו אם קשה לנו לגזור את {% equation %}f{% endequation %} עצמה).

ההוכחה עצמה מאוד קלה, בהינתן אוסף התנאים שנתתי. ראשית, בואו נזכיר חלק ממה שהמשפט היסודי של החדו"א אומר: אם {% equation %}g\left(x\right){% endequation %} <strong>רציפה</strong> בקטע {% equation %}\left[a,b\right]{% endequation %} אז הפונקציה {% equation %}G\left(x\right)=\int_{a}^{x}g\left(t\right)dt{% endequation %} גזירה ומקיימת {% equation %}G^{\prime}\left(x\right)=g\left(x\right){% endequation %} בכל הקטע. אצלנו נתון ש-{% equation %}g{% endequation %} אכן רציפה (בדיוק כדי שנוכל להשתמש בטענה הזו), אז מה שאנחנו רוצים להראות הוא ש-{% equation %}f\left(x\right){% endequation %} הוא {% equation %}G{% endequation %} הזו עד כדי קבוע, כלומר {% equation %}f\left(x\right)=G\left(x\right)+C{% endequation %}. בואו נעשה את זה.

מכיוון ש-{% equation %}f_{n}^{\prime}\to g{% endequation %} בהתכנסות במ"ש בתחום {% equation %}D=\left[a,b\right]{% endequation %} אפשר לקחת {% equation %}x\in D{% endequation %} שרירותי ולהשתמש במשפט על האינטגרל כדי להראות

{% equation %}\int_{a}^{x}f_{n}^{\prime}\left(t\right)dt\to\int_{a}^{x}g\left(t\right)dt{% endequation %}

עכשיו, מה זה האינטגרל {% equation %}\int_{a}^{x}f_{n}^{\prime}\left(t\right)dt{% endequation %}? כאן אנחנו משתמשים <strong>בנוסחת ניוטון-לייבניץ</strong>, שגם היא מסקנה מהמשפט היסודי: מכיוון ש-{% equation %}f_{n}{% endequation %} היא פונקציה קדומה של {% equation %}f_{n}^{\prime}{% endequation %} אז {% equation %}\int_{a}^{x}f_{n}^{\prime}\left(t\right)dt=f_{n}\left(x\right)-f_{n}\left(a\right){% endequation %} כלומר, אפשר גם לכתוב כך:

{% equation %}\int_{a}^{x}g\left(t\right)dt=\lim_{n\to\infty}\int_{a}^{x}f_{n}^{\prime}\left(t\right)dt{% endequation %}

{% equation %}=\lim_{n\to\infty}\left(f_{n}\left(x\right)-f_{n}\left(a\right)\right)=f\left(x\right)-f\left(a\right){% endequation %}

כשבשורה האחרונה השתמשנו בהתכנסות <strong>הנקודתית</strong> של {% equation %}f_{n}{% endequation %} אל {% equation %}f{% endequation %}.

אם כן, קיבלנו ש-{% equation %}G\left(x\right)=\int_{a}^{x}g\left(t\right)dt=f\left(x\right)-f\left(a\right){% endequation %} וזה בדיוק מה שרצינו: {% equation %}f\left(x\right)=G\left(x\right)+C{% endequation %} כאשר {% equation %}C=f\left(a\right){% endequation %}. זה מסיים את ההוכחה הזו, ומה שנשאר לנו לעשות הוא לראות דוגמא לכך שלא היינו יכולים ללכת על המשפט הפשוט יותר שהראיתי בהתחלה.

דרך פשוטה אחת ליצור דוגמא נגדית היא לקחת פונקציות "משוגעות", כאלו שמשתנות בקצב מאוד מהיר ולכן הנגזרת שלהן בעייתית, אבל לכפול אותן בגורם "מרגיע" שיגרום לכך שהגודל שלהן שואף לאפס - זה נותן לנו סדרה שכל איבר בה הוא משוגע, אבל השגעונות הללו נעלמים כשעוברים לגבול. 

סדרה אחת לדוגמא היא {% equation %}f_{n}\left(x\right)=\frac{1}{n}\sin\left(n^{2}x\right){% endequation %}. כאן ה-{% equation %}\frac{1}{n}{% endequation %} הוא הגורם המרגיע, אבל בתוך הסינוס יש לנו {% equation %}n^{2}{% endequation %} ש"משגע" את הסינוס וגורם לכך שככל ש-{% equation %}n{% endequation %} גדול יותר, הסינוס קופץ בין {% equation %}-1{% endequation %} ל-{% equation %}1{% endequation %} בקצב גבוה יותר. העניין פה הוא שתמיד מתקיים {% equation %}\left|\sin\left(n^{2}x\right)\right|\le1{% endequation %} ולכן כש-{% equation %}n{% endequation %} שואף לאינסוף {% equation %}f_{n}\left(x\right){% endequation %} שואפת לאפס במידה שווה: עבור {% equation %}\varepsilon>0{% endequation %} ניקח {% equation %}N=\frac{1}{\varepsilon}{% endequation %} ונקבל שעבור {% equation %}n>N{% endequation %} (ולכן {% equation %}\frac{1}{n}<\frac{1}{N}{% endequation %}) לכל {% equation %}x{% endequation %} מתקיים 

{% equation %}\left|f_{n}\left(x\right)\right|=\frac{1}{n}\left|\sin\left(n^{2}x\right)\right|\le\frac{1}{n}<\frac{1}{N}=\varepsilon{% endequation %}

מה שאומר ש-{% equation %}f_{n}\to0{% endequation %} ולכן אנחנו מצפים שיתקיים {% equation %}f_{n}^{\prime}\to0^{\prime}=0{% endequation %}.

מה קורה בפועל? כשאני גוזר פונקציה בסדרה אני מקבל {% equation %}f_{n}^{\prime}\left(x\right)=\frac{1}{n}\cos\left(n^{2}x\right)\cdot n^{2}=n\cos\left(n^{2}x\right){% endequation %}, ואם אני מציב {% equation %}x=0{% endequation %} אני מקבל {% equation %}f_{n}^{\prime}\left(0\right)=n{% endequation %}, כלומר {% equation %}f_{n}^{\prime}\left(0\right)\to\infty{% endequation %} ובוודאי שהגבול הוא לא 0, כך שסדרת הנגזרות <strong>לא</strong> מתכנסת לנגזרת של גבול הסדרה המקורית. זה מסיים את הדוגמא הנגדית הזו.

<h2>טורים של פונקציות</h2>

כל מה שעשינו עד עכשיו התייחס <strong>לסדרות</strong> של פונקציות אבל כבר ראינו במקרה של סדרות של מספרים שהמעבר לטורים הוא כמעט מיידי. אם יש לנו סדרה של פונקציות {% equation %}u_{0}\left(x\right),u_{1}\left(x\right),u_{2}\left(x\right),\ldots{% endequation %} אנחנו יכולים להגדיר פונקציות "סכום" {% equation %}f_{n}\left(x\right)=\sum_{k=0}^{n}u_{k}\left(x\right){% endequation %} ואז להגדיר את סכום הטור האינסופי של ה-{% equation %}u_{n}{% endequation %}-ים בתור {% equation %}\sum_{n=0}^{\infty}u_{n}\left(x\right)=\lim_{n\to\infty}f_{n}\left(x\right){% endequation %}. הדברים שראינו עבור סדרות של פונקציות עוברים אוטומטית בלי כמעט שום בעיה: יש לנו מושג של <strong>התכנסות במידה שווה</strong> של טור, שאומר שסדרת הסכומים החלקיים מתכנסת במידה שווה. אם טור של פונקציות רציפות מתכנס במידה שווה, אז הוא מתכנס לפונקציה רציפה (כי אם כל ה-{% equation %}u_{n}{% endequation %}--ים רציפים אז גם כל {% equation %}f_{n}{% endequation %} היא רציפה כי סכום <strong>סופי</strong> של פונקציות רציפות הוא פונקציה רציפה, ומכאן נשתמש בתוצאה על גבול של סדרות שכבר ראינו), והוא מקיים {% equation %}\int_{a}^{b}\sum_{n=0}^{\infty}u_{n}\left(x\right)=\sum_{n=0}^{\infty}\int_{a}^{b}u_{n}\left(x\right){% endequation %}, כלומר אפשר "להחליף את סדר הסכום האינסופי והאינטגרל" - הכללה של תכונת הלינאריות של אינטגרל שעובדת עבור סכומים סופיים.

בנוסף יש לנו תוצאה דומה עבור נגזרות, שכפי שראינו דורשת תנאים קצת שונים: אם {% equation %}\sum_{n=0}^{\infty}u_{n}{% endequation %} מתכנס נקודתית אל {% equation %}f{% endequation %} ולכל {% equation %}u_{n}{% endequation %} יש נגזרת אינטגרבילית {% equation %}u_{n}^{\prime}{% endequation %} וטור הנגזרות {% equation %}\sum_{n=0}^{\infty}u_{n}^{\prime}{% endequation %} מתכנס במ"ש, אז {% equation %}f^{\prime}=\sum_{n=0}^{\infty}u_{n}^{\prime}{% endequation %}, או בכתיב אחר - {% equation %}\left(\sum_{n=0}^{\infty}u_{n}\right)^{\prime}=\sum_{n=0}^{\infty}u_{n}^{\prime}{% endequation %}, כלומר אפשר להחליף את סדר הסכום האינסופי והנגזרת - הכללה של תכונת הלינאריות של נגזרת שעובדת עבור סכומים סופיים.

הנה דוגמא לאופן שבו משתמשים בזה. בפוסט שלי על <a href="https://gadial.net/2019/02/13/coupon_collector_problem/">בעיית איסוף הקופונים</a> צץ באופן טבעי כחלק מהפתרון שלנו הסכום {% equation %}\sum_{n=0}^{\infty}nx^{n-1}{% endequation %} שרצינו לחשב. מה שדי קופץ לעין כאן הוא שהאיבר הכללי של הסכום נראה כמו נגזרת: {% equation %}\left(x^{n}\right)^{\prime}=nx^{n-1}{% endequation %}. אז אני משתמש ב-{% equation %}\left(\sum_{n=0}^{\infty}u_{n}\right)^{\prime}=\sum_{n=0}^{\infty}u_{n}^{\prime}{% endequation %} כדי "להוציא את הנגזרת החוצה":

{% equation %}\sum_{n=0}^{\infty}nx^{n-1}=\sum_{n=0}^{\infty}\left(x^{n}\right)^{\prime}=\left(\sum_{n=0}^{\infty}x^{n}\right)^{\prime}{% endequation %}

זה טוב, בגלל שיש לי את הנוסחה {% equation %}\sum_{n=0}^{\infty}x^{n}=\frac{1}{1-x}{% endequation %} ואת הביטוי הזה קל לגזור: {% equation %}\left(\frac{1}{1-x}\right)^{\prime}=\frac{1}{\left(1-x\right)^{2}}{% endequation %}, מה שנותן לנו את התוצאה {% equation %}\sum_{n=0}^{\infty}nx^{n-1}=\frac{1}{\left(1-x\right)^{2}}{% endequation %}. אבל זה, כמובן, רק בתנאי שהתנאים של המשפט שלי מתקיימים: רק בתנאי שהטור {% equation %}\sum_{n=0}^{\infty}nx^{n-1}{% endequation %} מתכנס, ושהטור {% equation %}\sum_{n=0}^{\infty}x^{n}{% endequation %} מתכנס במ"ש. עכשיו, ברור שאם נציב {% equation %}x=1{% endequation %} ב-{% equation %}\sum_{n=0}^{\infty}x^{n}{% endequation %} נקבל את הטור {% equation %}\sum_{n=0}^{\infty}1{% endequation %} שלא מתכנס בכלל, אז אני צריך מלכתחילה להגביל את עצמי לתחום {% equation %}\left|x\right|<1{% endequation %} - אבל גם בתחום הזה, איך אני יודע שהטורים מתכנסים?

ספציפית עבור שני הטורים שאני מדבר עליהם כאן יש תורה שלמה ומרתקת שמתעסקת בהתכנסות שלהם שאגיע אליה בפוסט הבא, אבל עוד לפני שנגיע לתיאוריה של טורים ספציפיים יש משפט מועיל במיוחד שצריך להזכיר פה: מבחן ה-M של ויירשטראס.

הרעיון במבחן ה-M הוא פשוט: בואו נמיר את שאלת ההתכנסות במ"ש של טור פונקציות שהיא מסובכת, בשאלת התכנסות של טור <strong>מספרים</strong> שגם היא מסובכת אבל פחות.

המשפט אומר כך: נניח שיש לנו את טור הפונקציות {% equation %}\sum_{n=0}^{\infty}u_{n}{% endequation %} ויש סדרה {% equation %}\left\{ M_{n}\right\} _{n=0}^{\infty}{% endequation %}של מספרים אי שליליים כך ש-{% equation %}\left|u_{n}\left(x\right)\right|\le M_{n}{% endequation %} לכל {% equation %}x\in D{% endequation %} (כשכזכור {% equation %}D{% endequation %} הוא התחום שעליו כל ה-{% equation %}u_{n}{% endequation %} מוגדרות) ואם בנוסף לזה מתקיים שהטור {% equation %}\sum_{n=0}^{\infty}M_{n}{% endequation %} מתכנס (התכנסות רגילה של טורי מספרים) אז {% equation %}\sum_{n=0}^{\infty}u_{n}{% endequation %} מתכנס במ"ש ב-{% equation %}D{% endequation %}.

איך מוכיחים את זה? ראשית צריך להראות ש-{% equation %}\sum_{n=0}^{\infty}u_{n}{% endequation %} בכלל מתכנס אל <strong>משהו</strong>. ניקח {% equation %}x\in D{% endequation %} כלשהו ונסתכל על טור המספרים {% equation %}\sum_{n=0}^{\infty}\left|u_{n}\left(x\right)\right|{% endequation %}. עכשיו נשלוף שני דברים מהתורה של סכומים אינסופיים של מספרים:

<ul> <li>מבחן ההשוואה: אם {% equation %}0\le a_{n}\le b_{n}{% endequation %} לכל {% equation %}n{% endequation %} והטור {% equation %}\sum_{n=0}^{\infty}b_{n}{% endequation %} מתכנס, אז הטור {% equation %}\sum_{n=0}^{\infty}a_{n}{% endequation %} מתכנס.</li>


<li>אם {% equation %}\sum_{n=0}^{\infty}\left|a_{n}\right|{% endequation %} מתכנס אז {% equation %}\sum_{n=0}^{\infty}a_{n}{% endequation %} מתכנס (<strong>התכנסות בהחלט</strong> של טור גוררת התכנסות שלו).</li>

</ul>

אצלנו {% equation %}0\le\left|u_{n}\left(x\right)\right|\le M_{n}{% endequation %} בשילוב עם ההתכנסות של {% equation %}\sum_{n=0}^{\infty}M_{n}{% endequation %} ומבחן ההשוואה מראים שהטור {% equation %}\sum_{n=0}^{\infty}\left|u_{n}\left(x\right)\right|{% endequation %} מתכנס (עבור {% equation %}x\in D{% endequation %} ספציפי), ולכן {% equation %}\sum_{n=0}^{\infty}u_{n}\left(x\right){% endequation %} גם מתכנס. זה מאפשר לנו להגדיר פונקציה {% equation %}f\left(x\right)=\sum_{n=0}^{\infty}u_{n}\left(x\right){% endequation %} לכל {% equation %}x\in D{% endequation %}, ורק נשאר להראות ש-{% equation %}\sum_{n=0}^{\infty}u_{n}{% endequation %} מתכנס במ"ש אל {% equation %}f{% endequation %}; כלומר, שאם נגדיר {% equation %}f_{n}\left(x\right)=\sum_{k=0}^{n}u_{k}\left(x\right){% endequation %} אז סדרת הפונקציות {% equation %}f_{n}{% endequation %} מתכנסת במ"ש אל {% equation %}f{% endequation %}.

נוכיח את זה בצורה הרגילה: נאמר "יהא {% equation %}\varepsilon>0{% endequation %}" ועכשיו נרצה למצוא {% equation %}N{% endequation %} כך שאם {% equation %}n>N{% endequation %} אז {% equation %}\left|f\left(x\right)-f_{n}\left(x\right)\right|<\varepsilon{% endequation %} לכל {% equation %}x\in D{% endequation %}. זה דורש חישוב די ישיר:

{% equation %}\left|f\left(x\right)-f_{n}\left(x\right)\right|=\left|\sum_{n=0}^{\infty}u_{n}\left(x\right)-\sum_{k=0}^{n}u_{k}\left(x\right)\right|={% endequation %}

{% equation %}=\left|\sum_{k=n+1}^{\infty}u_{k}\left(x\right)\right|\le\sum_{k=n+1}^{\infty}\left|u_{k}\left(x\right)\right|\le\sum_{k=n+1}^{\infty}M_{k}{% endequation %}

עכשיו, מכיוון ש-{% equation %}\sum_{n=0}^{\infty}M_{n}{% endequation %} מתכנס, הזנב של הטור שואף לאפס (כי אם סכום הטור הוא {% equation %}L{% endequation %}, הזנב הוא הסדרה {% equation %}L-S_{n}{% endequation %} ומכיוון ש-{% equation %}S_{n}\to L{% endequation %} הסדרה הזו שואפת לאפס), כלומר לכל {% equation %}\varepsilon>0{% endequation %} קיים {% equation %}N{% endequation %} כך שאם {% equation %}n>N{% endequation %} אז {% equation %}\left|\sum_{k=n+1}^{\infty}M_{k}\right|\le\varepsilon{% endequation %}, מה שמסיים את ההוכחה (כי ה-{% equation %}M_{k}{% endequation %}-ים הם אי שליליים ולכן {% equation %}\left|\sum_{k=n+1}^{\infty}M_{k}\right|=\sum_{k=n+1}^{\infty}M_{k}{% endequation %}).

אם כן, אלו התוצאות הכלליות שבדרך כלל מציגים בתחילת הדיון על הנושאים הללו. בפוסט הבא אני אקפוץ אל סוג ספציפי של טורי פונקציות, שגם מתנהגים יפה יותר מאשר במקרה הכללי, והם גם שימושיים בצורה יוצאת מן הכלל - <strong>טורי חזקות</strong>. 