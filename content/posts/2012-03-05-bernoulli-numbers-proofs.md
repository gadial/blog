---
id: 1536
title: "מספרי ברנולי - ההוכחות"
date: 2012-03-05 13:53:05
layout: post
categories: 
  - תורת המספרים
tags: 
  - גם טכני זה כיף!
  - מספרי ברנולי
  - פונקציות יוצרות
  - פונקצית הזטא של רימן
---
בפוסט הקודם הצגתי כמה תוצאות יפות שקשורות למספרי ברנולי, אבל לא הוכחתי כלום. הפעם אני רוצה לדבר על החלק המעניין - איך מוכיחים את מקצת הדברים הללו. המטרה שלי כאן היא כפולה - לא רק להראות לכם איך מוכיחים תוצאות ספציפיות, אלא בעיקר להראות לכם <strong>למה</strong> זה בכלל מעניין לראות הוכחות. הסיבות שלי פשוטות: לראות את ההוכחה גם מאפשר לנו להבין הרבה יותר טוב <strong>למה</strong> התוצאה נכונה; גם מאפשר לנו להבין יותר טוב באופן כללי את האובייקט שאנחנו מדברים עליו ואיך הוא מתקשר לשאר היקום; וגם יש בהוכחה אלגנטיות ואסתטיות משל עצמה. שימו לב שהמטרה ה"רשמית" של הוכחות - לדעת שהתוצאה נכונה - היא אפילו לא מטרה משנית שלי כאן; אני בטוח שהקוראים מאמינים לי שהתוצאות בפוסט הקודם היו נכונות ושאני לא עובד עליהם. אז בואו נבהיר את זה חד משמעית - אנחנו מתעניינים כאן בהוכחות כי הן <strong>החלק היפה</strong> של המתמטיקה. באנלוגיה, בפוסט הקודם הפלאנו בשבחם של מוצארט ובאך ובטהובן ואמרנו כמה שהמוזיקה שלהם יפה ומעניינת ומוצלחת; בפוסט הזה אנחנו הולכים להקשיב למוזיקה.

רק מה, כמו עם באך ומוצארט ובטהובן, קשה להקשיב למוזיקה בלי קצת ידע ונסיון מוקדמים. אז אני מזהיר מראש - הפוסט הזה לא מרחם. הוא מניח ידע כלשהו באנליזה, ויהיו דברים שאגיד ללא הסבר מתוך הנחה שהקורא יודע להשלים בעצמו. אני מתנצל מראש בפני מי שיאבד אותי - אתם מוזמנים לשאול שאלות בתגובות (והכי חשוב, להגיד מה הרגע הראשון שבו איבדתם אותי).

נתחיל מתזכורת, כדי שהנוסחה תהיה לנו מול העיניים: מספרי ברנולי מוגדרים רקורסיבית על ידי {% equation %}B_{0}=1{% endequation %} והנוסחה

{% equation %}B_{n}=-\frac{1}{n+1}\sum_{k=0}^{n-1}{n+1 \choose k}B_{k}{% endequation %}

הנוסחה הזו מאפשרת לנו לחשב בנוחות יחסית ערכים של {% equation %}B_{n}{% endequation %}, אבל יש דרך טובה ממנה לייצג את כל הסדרה {% equation %}B_{n}{% endequation %} "בבת אחת" - <strong>פונקציה יוצרת</strong>. באופן כללי, הרעיון שמאחורי פונקציה יוצרת של סדרה כלשהי היא לקחת את ערכי הסדרה ו"לשתול" אותם בתור מקדמים בתוך טור חזקות; טור החזקות הזה מגדיר פונקציה, ואם אנחנו יודעים משהו על המקדמים יש תקווה שנקבל צורת הצגה פשוטה יחסית לפונקציה הזו. מרגע שיש לנו צורת הצגה פשוטה שכזו, אנחנו מסוגלים לתקוף את הפונקציה הזו עם כלים שאנחנו מכירים מאנליזה, ולהסיק מסקנות על אברי הסדרה המקורית. זו דרך התבוננות מאוד לא טריוויאלית על סדרות, ומספרי ברנולי הם הזדמנות מצויינת להמחיש עד כמה היא בעצם חזקה.

יש כמה סוגים שונים של פונקציות יוצרות ובהקשר שלנו הפונקציה היוצרת שבה כדאי להשתמש, כי הצורה שלה פשוטה, היא מה שנקרא <strong>פונקציה יוצרת אקספוננציאלית</strong>. הפונקציה היוצרת האקספוננציאלית של הסדרה {% equation %}a_{0},a_{1},a_{2},\dots{% endequation %} היא {% equation %}f\left(x\right)=\sum_{n=0}^{\infty}a_{n}\frac{x^{n}}{n!}{% endequation %}. ההבדל בינה ובין פונקציה יוצרת "רגילה", למי שמכיר, הוא החלוקה ב-{% equation %}n!{% endequation %}. כעת, התכונה החשובה של פונקציות יוצרות היא מה שקורה להן בפעולת הכפל; את זה אני רוצה להראות לכם במפורש. נניח שיש לנו שתי פונקציות יוצרות אקספוננציאליות ואנו כופלים אותן:

{% equation %}\left(\sum_{k=0}^{\infty}a_{k}\frac{x^{k}}{k!}\right)\left(\sum_{m=0}^{\infty}b_{m}\frac{x^{m}}{m!}\right)=\sum_{n=0}^{\infty}c_{n}\frac{x^{n}}{n!}{% endequation %}

מהו {% equation %}c_{n}{% endequation %}?

לצורך כך, השאלה היא אילו גורמים מתוך המכפלה נותנים לנו את {% equation %}\frac{x^{n}}{n!}{% endequation %} עם מקדם כלשהו. די ברור שזה קורה לכל {% equation %}k,m{% endequation %} שמקיימים {% equation %}k+m=n{% endequation %}. גורם כזה יתן לנו את המכפלה

{% equation %}\left(a_{k}\frac{x^{k}}{k!}\right)\left(b_{m}\frac{x^{m}}{m!}\right)=a_{k}b_{m}\frac{x^{k+m}}{k!m!}=a_{k}b_{m}\frac{n!}{k!m!}\frac{x^{n}}{n!}=a_{k}b_{n-k}{n \choose k}\frac{x^{n}}{n!}{% endequation %}

ולכן המקדם של {% equation %}\frac{x^{n}}{n!}{% endequation %} בסך הכל יהיה {% equation %}c_{n}=\sum_{k=0}^{n}{n \choose k}a_{k}b_{n-k}{% endequation %}. לדבר הזה קוראים <strong>קונבולוציה בינומית</strong> של הסדרות {% equation %}a_{n},b_{n}{% endequation %}, וזה הולך להיות שימושי למדי בהמשך.

אם כן, אני מגדיר פונקציה {% equation %}f\left(z\right)=\sum_{n=0}^{\infty}B_{n}\frac{z^{n}}{n!}{% endequation %} (אני משתמש ב-{% equation %}z{% endequation %} כי בקרוב נתחיל לחשוב על {% equation %}f{% endequation %} כפונקציה מרוכבת). השאלה הראשונה היא האם יש לנו דרך הצגה פשוטה עבור הפונקציה הזו. ראשית, שימו לב שאת הנוסחה הרקורסיבית למספרי ברנולי שהצגתי למעלה אפשר לנסח גם באופן האלגנטי הבא: {% equation %}\sum_{k=0}^{n}{n+1 \choose k}B_{k}=0{% endequation %} עבור {% equation %}n\ge1{% endequation %} (מה ההבדלים? למה זה נכון?). הדבר הזה, אם תשימו לב, מזכיר באופן חשוד את הנוסחה לקונבולוציה בינומית שהצגתי למעלה, רק שבמקום {% equation %}{n \choose k}{% endequation %} יש לנו מקדם של {% equation %}{n+1 \choose k}{% endequation %}. יש דרך מאוד נקיה לפתור את הבעיה הזו: נגדיר סדרה {% equation %}a_{m}{% endequation %} על ידי {% equation %}a_{0}=0{% endequation %} ו-{% equation %}a_{m}=1{% endequation %} לכל {% equation %}m&gt;0{% endequation %}, וכעת {% equation %}\sum_{k=0}^{n}{n+1 \choose k}B_{k}=\sum_{k=0}^{n+1}{n+1 \choose k}B_{k}a_{n+1-k}=0{% endequation %} לכל {% equation %}n&gt;0{% endequation %}. במילים אחרות, אם {% equation %}g\left(z\right){% endequation %} היא הפונקציה היוצרת של הסדרה {% equation %}a_{m}{% endequation %} שנתתי, אז פונקציה היוצרת {% equation %}f\left(z\right)g\left(z\right){% endequation %} כמעט כל המקדמים הם 0, למעט אולי שני הראשונים עבור {% equation %}n=0,1{% endequation %}.

אותם אפשר לחשב במפורש: המקדם עבור {% equation %}n=0{% endequation %} הוא {% equation %}{0 \choose 0}B_{0}a_{0}=0{% endequation %}, והמקדם עבור {% equation %}n=1{% endequation %} הוא {% equation %}{1 \choose 0}B_{0}a_{1}+{1 \choose 1}B_{1}a_{0}=1{% endequation %}. לכן {% equation %}f\left(z\right)g\left(z\right)=z{% endequation %} (כאן {% equation %}z{% endequation %} הוא טור חזקות אינסופי שבו כל המקדמים הם 0 למעט המקדם של {% equation %}z{% endequation %}). אבל מהו {% equation %}g\left(z\right){% endequation %}? או, זה קל במיוחד. הטור שמתאים לסדרה ש<strong>כל</strong> אבריה הם 1 הוא פשוט {% equation %}\sum_{n=0}^{\infty}\frac{z^{n}}{n!}=e^{z}{% endequation %}, ולכן, אם המקדם הראשון הוא 0, אז הפונקציה היוצרת האקספוננציאלית המתאימה היא {% equation %}e^{z}-1{% endequation %}.

אם לסכם: {% equation %}f\left(z\right)\left(e^{z}-1\right)=z{% endequation %}, כלומר {% equation %}f\left(z\right)=\frac{z}{e^{z}-1}{% endequation %}. גילינו את הפונקציה היוצרת האקספוננציאלית של מספרי ברנולי כמעט בלי חישובים "כבדים", רק מתוך ההיכרות שלנו עם המושג של קונבולוציה בינומית (ברוב ההוכחות שיצא לי לראות פשוט עושים את החישובים וחסל, וזה יוצא מסורבל וחבל).

עכשיו אפשר להשתמש בפונקציה היוצרת הזו כדי להוכיח חלק מהטענות שטענתי על מספרי ברנולי בפוסט הקודם. נתחיל מהעיקר: הסכומים {% equation %}S_{m}\left(n\right)=0^{m}+1^{m}+\dots+\left(n-1\right)^{m}=\sum_{k=0}^{n-1}k^{m}{% endequation %}.

התעלול שבו אנחנו משתמשים הוא פשוט, אבל הרעיון שלפיו נשתמש בו הוא מקסים לגמרי: נראה כנראה טבעי לחשוב על {% equation %}m{% endequation %} בתור מספר קבוע ולהתבונן בסדרה {% equation %}S_{m}\left(0\right),S_{m}\left(1\right),S_{m}\left(2\right),\dots{% endequation %}, אבל מה שנעשה יהיה בדיוק את ההפך: נקבע את {% equation %}n{% endequation %} דווקא, ונקבל סדרת מספרים {% equation %}S_{0}\left(n\right),S_{1}\left(n\right),S_{2}\left(n\right),\dots{% endequation %}. יש לנו סדרת מספרים? יופי. בואו נסתכל בפונקציה היוצרת האקספוננציאלית שלה!

זה רעיון מבריק, כי הפונקציה היוצרת האקספוננציאלית היא פשוטה למדי. כדי לראות את זה, ניעזר בעוד תכונה פשוטה של פונקציות יוצרות: הפונקציה שהיא סכומן, מתאימה לסדרה שהאיבר הכללי בה הוא סכום הסדרות של הפונקציות היוצרות הללו. כעת, {% equation %}S_{m}\left(n\right)=0^{m}+1^{m}+2^{m}+\dots+\left(n-1\right)^{m}{% endequation %} ולכן אפשר לחשוב על הסדרה {% equation %}S_{m}\left(n\right){% endequation %} בתור סכום של {% equation %}n{% endequation %} סדרות: הסדרה {% equation %}0^{0},0^{1},0^{2},\dots{% endequation %}; הסדרה {% equation %}1^{0},1^{1},1^{2},\dots{% endequation %} וכן הלאה.

הפונקציה היוצרת האקספוננציאלית של הסדרה {% equation %}k^{0},k^{1},k^{2},\dots{% endequation %} קלה לחישוב באופן ישיר: היא פשוט {% equation %}\sum_{m=0}^{\infty}k^{m}\frac{z^{m}}{m!}=e^{kz}{% endequation %}. לכן הפונקציה היוצרת של {% equation %}S_{m}\left(n\right){% endequation %} היא {% equation %}\sum_{k=0}^{n-1}e^{kz}=\frac{e^{nz}-1}{e^{z}-1}{% endequation %} - זהו פשוט סכום של סדרה הנדסית רגילה.

עכשיו, {% equation %}\frac{e^{nz}-1}{e^{z}-1}{% endequation %} די דומה ל-{% equation %}\frac{z}{e^{z}-1}{% endequation %}; למעשה, {% equation %}\frac{e^{nz}-1}{e^{z}-1}=\frac{z}{e^{z}-1}\cdot\frac{e^{nz}-1}{z}{% endequation %}. כל שנותר לנו לעשות הוא להבין איך נראית הסדרה שהפונקציה היוצרת האקספוננציאלית שלה היא {% equation %}\frac{e^{nz}-1}{z}{% endequation %}, לבצע קונבולוציה בינומית לסדרה הזו עם סדרת מספרי ברנולי, וסיימנו.

כדי להבין את מי {% equation %}\frac{e^{nz}-1}{z}{% endequation %} מייצג, הכי פשוט לפתח את הפונקציה הזו לטור טיילור, תוך שימוש בכך שאנחנו מכירים את טור הטיילור של {% equation %}e^{nz}{% endequation %}. נקבל {% equation %}\frac{e^{nz}-1}{z}=\sum_{k=0}^{\infty}n^{k+1}\frac{z^{k}}{\left(k+1\right)!}=\sum_{k=0}^{\infty}\left(k+1\right)^{-1}n^{k+1}\frac{z^{k}}{k!}{% endequation %}. במילים אחרות, הפונקציה היוצרת הזו מייצגת בדיוק את הסדרה {% equation %}\left(k+1\right)^{-1}n^{k+1}{% endequation %} (כש-{% equation %}k{% endequation %} רץ מאפס עד אינסוף). לכן על ידי קונבולוציה בינומית עם מספרי ברנולי נקבל:

{% equation %}S_{m}\left(n\right)=\sum_{k=0}^{m}{m \choose k}B_{k}\left(m-k+1\right)^{-1}n^{m-k+1}=\frac{1}{m+1}\sum_{k=0}^{m}{m+1 \choose k}B_{k}n^{m+1-k}{% endequation %}

קיבלנו בדיוק את הנוסחה ל-{% equation %}S_{m}\left(n\right){% endequation %} שהבטחתי. בתקווה עכשיו היא גם לא נראית לכם כמו ג'יבריש אחד גדול, אלא כמו מה שהיא - קונבולציה בינומית של מספרי ברנולי עם... עוד משהו.

הבה ונעבור לדבר הבא.

מה שאני רוצה לעשות עכשיו הוא להראות מה קורה כשחושבים על הפונקציה היוצרת {% equation %}\frac{z}{e^{z}-1}{% endequation %} של מספרי ברנולי בתור פונקציה מרוכבת, חוקרים אותה עם כלים סטנדרטיים של אנליזה מרוכבת ומסיקים מסקנות על מספרי ברנולי. אגלה מראש שהתוצאה תהיה הנוסחה עבור {% equation %}\zeta\left(2n\right){% endequation %} לכל {% equation %}n{% endequation %} טבעי. אל תגידו לי שזה לא מפתיע.

באנליזה מרוכבת, פונקציה כמו {% equation %}f\left(z\right)=\frac{z}{e^{z}-1}{% endequation %} נקראת <strong>מרומורפית</strong>. זו פונקציה שהיא גזירה כמעט בכל מקום למעט נקודות בעייתיות מבודדות שבהן היא "מתפוצצת". זו כמובן לא הגדרה ברורה במיוחד; לצורך העניין מספיק לי להשתמש בהגדרה החצי-פורמלית לפיה פונקציה מרומורפית היא מנה של שתי פונקציות אנליטיות, כשפונקציה אנליטית היא פונקציה מרוכבת שגזירה בכל מקום. {% equation %}z{% endequation %} ו-{% equation %}e^{z}-1{% endequation %} הן פונקציות פשוטות ביותר ולא קשה להראות שהן אנליטיות.

איפה {% equation %}\frac{z}{e^{z}-1}{% endequation %} כן בעייתית? מן הסתם, בנקודות שבהן {% equation %}e^{z}-1=0{% endequation %}. אפשר להגדיר שהפונקציה שווה לאינסוף בנקודות אלו - יש לכך אפילו פורמליזם מאוד קונקרטי - ולכן זה לא מדויק לומר שהיא לא מוגדרת בהן; אבל ה"התפוצצות" שלה בנקודות הללו היא כן תופעה חריגה וחשובה. לנקודות כאלו קוראים <strong>קטבים</strong> של הפונקציה. במקרה שלנו, יש לפונקציה קוטב כאשר {% equation %}e^{z}=1{% endequation %}. כעת, זכרו שמדובר פה על פונקציות מרוכבות, ושהאקספוננט המרוכב מקיים {% equation %}e^{a+bi}=e^{a}\left(\cos b+i\sin b\right){% endequation %}. לכן אם {% equation %}e^{a+bi}=1{% endequation %}, בהכרח {% equation %}a=0{% endequation %} ו-{% equation %}\cos b=1{% endequation %} ו-{% equation %}\sin b=0{% endequation %}, ולכן {% equation %}z=2i\pi k{% endequation %}, עבור {% equation %}k\in\mathbb{Z}{% endequation %} כלשהו.

ועכשיו קורה קסם!

לקסם הזה יש שם - "משפט השארית", והוא בדרך כלל הפסגה של קורס מבוא לאנליזה מרוכבת, ולכן לא אנסה להציג אותו כאן כרגע. הרעיון במשפט השארית הוא שאפשר לדעת את הערך של אינטגרל על מסלול סגור של פונקציה מרומורפית כלשהי רק על פי מה שקורה לפונקציה הזו בקטבים שלה שנמצאים בתוך התחום שהמסלול הסגור כולא (ובכלל לא חשוב מה הצורה של המסלול הזה). קצת יותר במדויק, לכל קוטב של הפונקציה מתאים מספר כלשהו - ה<strong>שארית</strong> של הפונקציה בקוטב (פורמלית אפשר להגדיר אותו בטור המקדם של {% equation %}z^{-1}{% endequation %} בטור לורן של הפונקציה סביב הקוטב, אבל זה לא יגיד כלום למי שלא יודע כבר מה זה), והערך של האינטגרל הוא פשוט סכום השאריות הללו.

מהקסם הזה נובעת - לא מייד, אבל גם זה יצטרך לחכות לפעם אחרת - הנוסחה הבאה למקדמים של הפיתוח של {% equation %}\frac{z}{e^{z}-1}{% endequation %} סביב 0: {% equation %}B_{n}=-n!\sum_{k\in\mathbb{Z}\backslash\left\{ 0\right\} }a_{k}^{-n}{% endequation %}, כש-{% equation %}a_{k}=2i\pi k{% endequation %} הם הקטבים של הפונקציה (במקרה הספיציפי של הפונקציה הזו יוצא שהשארית בקוטב היא הקוטב עצמו, ומכאן ההופעה שלהם כאן - אבל כאמור, זה לא סוף הסיפור). למרות שנראה שאני מרמה כאן, זו אחת הטכניקות הבסיסיות והחשובות ביותר בעבודה עם פונקציות יוצרות - אם מצליחים לעשות אנליזה מעניינת לפונקצה היוצרת, אפשר ללמוד משהו על הסדרה שמתאימה לה מתוך התכונות האנליטיות של הפונקציה היוצרת - במקרה שלנו, הקטבים שלה.

מרגע שקיבלנו את {% equation %}B_{n}=-n!\sum_{k\in\mathbb{Z}\backslash\left\{ 0\right\} }a_{k}^{-n}{% endequation %} השאר נובע מאליו די מהר. ראשית, שימו לב שזו עוד הוכחה לכך שמספרי ברנולי האי-זוגיים הגדולים מ-1 הם אפס, פשוט כי אז {% equation %}a_{k}^{-n}=-a_{-k}^{-n}{% endequation %} ולכן הסכום מורכב כולו מזוגות של איברים שמבטלים זה את זה (עבור {% equation %}n=1{% endequation %} זה לא קורה פשוט כי הנוסחה לא תקפה עבור {% equation %}n=1{% endequation %}). אם לעומת זאת {% equation %}n{% endequation %} זוגי, בואו נסמן אותו בתור {% equation %}2n{% endequation %} כדי להקל על העניינים. עכשיו, {% equation %}a_{k}^{-2n}=a_{-k}^{-2n}=2^{-2n}\pi^{-2n}i^{-2n}\cdot\frac{1}{k^{2n}}{% endequation %} ו-{% equation %}i^{-2n}=\left(i^{2}\right)^{-n}=\left(-1\right)^{-n}=\left(-1\right)^{n}{% endequation %}, ולכן {% equation %}a_{k}^{-2n}+a_{-k}^{-2n}=2^{1-2n}\pi^{-2n}\left(-1\right)^{-n}\frac{1}{k^{2n}}{% endequation %}. לכן כשניקח את הסכום, נקבל:

{% equation %}B_{2n}=-\left(2n\right)!2^{1-2n}\pi^{-2n}\left(-1\right)^{-n}\sum_{k=1}^{\infty}\frac{1}{k^{2n}}{% endequation %}

אבל - מה זה הסכום הזה בסוף? זו בדיוק פונקצית הזטא של רימן! {% equation %}\sum_{k=1}^{\infty}\frac{1}{k^{2n}}=\zeta\left(2n\right){% endequation %}. לכן על ידי העברת אגפים מקבלים:

{% equation %}\zeta\left(2n\right)=\left(\left(-1\right)^{n+1}\frac{2^{2n-1}}{\left(2n\right)!}B_{2n}\right)\pi^{2n}{% endequation %}

וזו בדיוק הנוסחה שהבטחתי בפוסט הקודם. די מטורף, העניין הזה.

מתוך הערכים הללו של פונקציית הזטא, אפשר להסיק גם את הערכים שלה בנקודות השלמות השליליות, אם משתמשים בכלי החזק שרימן הוכיח את קיומו - המשוואה הפונקציונלית של פונקציית הזטא. הזכרתי את העסק בפוסט שעסק בהשערת רימן, אבל הנה תזכורת קטנה. ראשית, אני רוצה שתכירו חברה טובה של פונקציית הזטא, פונקציית הגמא {% equation %}\Gamma\left(z\right){% endequation %}. זו פונקציה מרוכבת שמהווה מעין הכללה של פונקציית העצרת ל(כמעט) כל המספרים המרוכבים, ובפרט מקיימת {% equation %}\Gamma\left(n\right)=\left(n-1\right)!{% endequation %} אם {% equation %}z=n{% endequation %} הוא מספר טבעי. כשמערבבים אותן ביחד, פונקציות הזטא והגמא מקיימות תכונת סימטריה מאוד יפה. נגדיר {% equation %}\xi\left(z\right)=\frac{1}{2}\pi^{-\frac{z}{2}}z\left(z-1\right)\Gamma\left(\frac{z}{2}\right)\zeta\left(z\right){% endequation %}, אז מתקיים:

{% equation %}\xi\left(z\right)=\xi\left(1-z\right){% endequation %}

זו תוצאה חשובה באופן כללי; עבורנו היא מעניינת אם נציב {% equation %}z=2n{% endequation %} (כש-{% equation %}n\ge1{% endequation %} הוא טבעי). במקרה הזה נקבל ש-{% equation %}\xi\left(2n\right)=\xi\left(-\left(2n-1\right)\right){% endequation %}. כאן {% equation %}-\left(2n-1\right){% endequation %} הוא מספר שלם שלילי אי זוגי <strong>כלשהו</strong>, עבור בחירה מתאימה של {% equation %}n{% endequation %}. בואו נראה מה בדיוק נקבל במשוואה הפונקציונלית אחרי הצבה:

{% equation %}\pi^{-\frac{2n}{2}}\left(2n\right)\left(2n-1\right)\Gamma\left(\frac{2n}{2}\right)\zeta\left(2n\right)=\pi^{-\frac{1-2n}{2}}\left(1-2n\right)\left(-2n\right)\Gamma\left(\frac{1-2n}{2}\right)\zeta\left(1-2n\right){% endequation %}

ולאחר פישוט:

{% equation %}\zeta\left(1-2n\right)=\pi^{\frac{1}{2}}\pi^{-2n}\Gamma\left(n\right)\Gamma\left(\frac{1-2n}{2}\right)^{-1}\zeta\left(2n\right){% endequation %}

מה זה {% equation %}\Gamma\left(n\right){% endequation %} אנחנו יודעים - {% equation %}\left(n-1\right)!{% endequation %}. אבל מה זה {% equation %}\Gamma\left(\frac{1-2n}{2}\right){% endequation %}? למרבה המזל, אני יכול לשלוף את הנוסחה מהשרוול: {% equation %}\Gamma\left(\frac{1}{2}-n\right)=\frac{\left(-4\right)^{n}n!}{\left(2n\right)!}\pi^{\frac{1}{2}}{% endequation %}. נראה קצת מפחיד, אבל אתם הרי <strong>יודעים</strong> שהכל כבר הולך להצטמצם.

אם כן, נקבל:

{% equation %}\pi^{\frac{1}{2}}\pi^{-2n}\Gamma\left(n\right)\Gamma\left(\frac{1-2n}{2}\right)^{-1}\zeta\left(2n\right)=\left(-1\right)^{n}\pi^{\frac{1}{2}}\pi^{-2n}\left(n-1\right)!\frac{\left(2n\right)!}{4^{n}n!}\pi^{-\frac{1}{2}}\zeta\left(2n\right)=\left(-1\right)^{n}\pi^{-2n}\frac{\left(2n\right)!}{n\cdot4^{n}}\zeta\left(2n\right){% endequation %}

נשאר רק להציב את הנוסחה ל-{% equation %}\zeta\left(2n\right){% endequation %} שכבר מצאנו, ולקבל:

{% equation %}\left(-1\right)^{n}\pi^{-2n}\frac{\left(2n\right)!}{n\cdot4^{n}}\zeta\left(2n\right)=-\frac{B_{2n}}{2n}{% endequation %}

מסקנה: {% equation %}\zeta\left(-\left(2n-1\right)\right)=-\frac{B_{2n}}{2n}{% endequation %}. אפשר לנסח את זה גם באופן טיפה שונה: {% equation %}\zeta\left(-n\right)=-\frac{B_{n+1}}{n+1}{% endequation %}, שהוא זה שהצגתי בפוסט הקודם.

לא הוכחתי את כל מה שדיברתי עליו בפוסט הקודם, אבל נראה לי שאפשר לעצור כאן. אני רוצה להדגיש שהעבודה הטכנית של כל מני הצבות וחישובים היא בדיוק זה - עבודה טכנית, ולא החלק המעניין כאן (אבל משהו שצריך לדעת לעשות ולא לפחד ממנו). מה שהיה באמת יפה ביותר כאן, לטעמי, הוא הרעיון של שימוש בפונקציה היוצרת של מספרי ברנולי והקסמים שנובעים מכך.
