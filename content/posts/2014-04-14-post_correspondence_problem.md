---
id: 3094
title: "פוסט של בעיית ההתאמה של פוסט"
date: 2014-04-14 14:41:09
layout: post
categories: 
  - חישוביות
tags: 
  - בעיית ההתאמה של פוסט
  - דקדוקים
  - רדוקציות
social_media_share: true
---
"בעיית ההתאמה של פוסט" - Post Correspondence Problem, ובקיצור PCP - היא בעיה נחמדה במדעי המחשב שנקראת על שם אמיל פוסט, אחד מחלוצי מדעי המחשב (ואינה קשורה לדואר, כמו שחשבתי הרבה זמן) שתיאר אותה ב-1946. מה שנחמד בבעיה הזו הוא שהיא <strong>בלתי פתירה</strong>, דהיינו לא קיים אלגוריתם שיודע לפתור אותה; זה נשמע כמו חסרון, אבל למי שמעוניינים להוכיח שעוד בעיות במדעי המחשב הן לא פתירות זה דווקא יתרון: כדי להראות שבעיה במדעי המחשב אינה פתירה, מספיק להראות טיעון מהצורה "אם הבעיה שלי הייתה פתירה, אז היינו יכולים לפתור בעזרתה את בעיית ההתאמה של פוסט". מה שטוב בבעיית ההתאמה של פוסט הוא שמצד אחד היא לא פתירה, אבל מצד שני היא מאוד פשוטה לניסוח, ולכן הוכחות של "כך אני פותר את פוסט, בהינתן פתרון לבעיה המוזרה שלי" הן קלות יחסית.

איך מוגדרת הבעיה? ההגדרה קצת מוזרה, אז נתחיל עם דוגמה. בואו נסתכל על שלושה זוגות של מילים מעל {% equation %}\left\{ 0,1\right\} {% endequation %} (כלומר, סדרות של 0 ו-1):

{% equation %}\left(00,0\right),\left(1,00\right),\left(0,10\right){% endequation %}

שתי מילים אפשר <strong>לשרשר</strong> - לכתוב אותן אחת אחרי השניה. השרשור של 00 עם 01 הוא המילה 0001. אז גם זוגות נשרשר "רכיב רכיב", כלומר {% equation %}\left(00,0\right)\cdot\left(1,00\right)=\left(001,000\right){% endequation %}. עכשיו, הבה ונסתכל על סדרת השרשורים הבאים:

{% equation %}\left(00,0\right)\cdot\left(00,0\right)\cdot\left(1,00\right)\cdot\left(0,10\right)=\left(000010,000010\right){% endequation %}

שימו לב מה קיבלתי - זוג שבו המילה בצד ימין והמילה בצד שמאל הן<strong> זהות</strong>, למרות שבכל הזוגות שמהם בניתי אותו המילים הללו תמיד שונות.

בואו נתאר את זה בצורה טיפה יותר פורמלית. נסמן את הזוגות בתור {% equation %}\left(a_{1},b_{1}\right),\left(a_{2},b_{2}\right),\left(a_{3},b_{3}\right){% endequation %}. למשל, {% equation %}b_{3}=10{% endequation %} ו-{% equation %}a_{2}=1{% endequation %}. אז האבחנה שלעיל היא בעצם האבחנה ש-{% equation %}a_{1}a_{1}a_{2}a_{3}=b_{1}b_{1}b_{2}b_{3}{% endequation %}. עוד יותר פורמלית: מצאנו <strong>סדרת אינדקסים </strong>{% equation %}j_{1},j_{2},\dots,j_{k}{% endequation %} כך ש-{% equation %}a_{j_{1}}a_{j_{2}}\cdots a_{j_{k}}=b_{j_{1}}b_{j_{2}}\cdots b_{j_{k}}{% endequation %}.

אצלנו {% equation %}n=4{% endequation %} ו-{% equation %}j_{1}=j_{2}=1{% endequation %}, {% equation %}j_{3}=2{% endequation %} ו-{% equation %}j_{4}=3{% endequation %}.

הדוגמה הזו בעצם מתארת כמעט לגמרי מה קורה באופן כללי: הקלט לבעיה הוא סדרה <strong>סופית</strong> של זוגות, {% equation %}\left(a_{1},b_{1}\right),\dots,\left(a_{n},b_{n}\right){% endequation %}, שכולן מעל אותו א"ב (הוא יכול להיות שונה מ-{% equation %}\left\{ 0,1\right\} {% endequation %} ובהמשך אשתמש בזה, אבל זה לצורך נוחות בלבד; אפשר היה בתיאוריה לעשות את הכל גם עם 0,1). השאלה היא האם קיימת סדרת אינדקסים <strong>סופית</strong> {% equation %}j_{1},\dots,j_{k}{% endequation %} כך ש-{% equation %}a_{j_{1}}a_{j_{2}}\cdots a_{j_{k}}=b_{j_{1}}b_{j_{2}}\cdots b_{j_{k}}{% endequation %}. כן או לא. זה הכל. והבעיה האלגוריתמית הזו - אינה כריעה.

המטרה העיקרית שלי בפוסט היא להציג את הוכחת אי הכריעות של הבעיה, שהיא נפלאה לטעמי, אבל לפני כן אני רוצה להראות את היישום הסטנדרטי של הבעיה להוכחת אי הכריעות של בעיה אחרת - ובעיה טבעית ומעניינת למדי: בדיקה האם דקדוק חופשי-הקשר הוא דו-משמעי. זה מצריך ממני להציג בזריזות את ההגדרה של דקדוק חופשי-הקשר, שעדיין לא הצגתי בבלוג בכללת אבל אפשר גם לראות אותה ב<a href="http://he.wikipedia.org/wiki/%D7%93%D7%A7%D7%93%D7%95%D7%A7_%D7%97%D7%95%D7%A4%D7%A9%D7%99-%D7%94%D7%A7%D7%A9%D7%A8">ויקיפדיה</a>. אני חושב על דקדוק בתור מעין מכונה ליצירת מילים: מתחילים מאיזה <strong>משתנה</strong> התחלתי {% equation %}S{% endequation %}, ומבצעים סדרה של <strong>גזירות</strong>, כאשר כל גזירה מחליפה משתנה במילה שיש לנו כרגע בתת-מילה חדשה, שמכילה משתנים חדשים וסימבולים (<strong>טרמינלים</strong>) שאי אפשר לגזור. דקדוק {% equation %}G=\left(V,T,S,P\right){% endequation %} כולל קבוצה סופית {% equation %}V{% endequation %} של משתנים, קבוצה סופית {% equation %}T{% endequation %} של טרמינלים, משתנה התחלתי {% equation %}S\in V{% endequation %} וקבוצה סופית {% equation %}P{% endequation %} של כללי גזירה שמסומנים {% equation %}A\to\beta{% endequation %} כאשר {% equation %}A{% endequation %} הוא המשתנה שגוזרים ו-{% equation %}\beta{% endequation %} היא מילה שיכולה לכלול משתנים וטרמינלים.

בואו נסתכל לדוגמה על דקדוק טיפשי לגזירת ביטויים חשבוניים. הטרמינלים שלנו יהיו {% equation %}0,1,2,\dots,9,+,\times{% endequation %}. יהיה לנו רק משתנה אחד: {% equation %}S{% endequation %} עצמו. ויהיו לנו כללי גזירה מהצורה {% equation %}S\to0,S\to1,\dots,S\to9{% endequation %} וכמו כן את {% equation %}S\to S+S{% endequation %} ואת {% equation %}S\to S\times S{% endequation %}. עכשיו בואו ונראה שתי גזירות למילה {% equation %}1+2\times3{% endequation %}:

{% equation %}S\Rightarrow S+S\Rightarrow1+S\Rightarrow1+S\times S\Rightarrow1+2\times S\Rightarrow1+2\times3{% endequation %}

{% equation %}S\Rightarrow S\times S\Rightarrow S\times3\Rightarrow S+S\times3\Rightarrow S+2\times3\Rightarrow1+2\times3{% endequation %}

שתי הגזירות הללו שונות זו מזו באופן מהותי. ההסבר הפורמלי הוא שיש להן עצי גזירה שונים אבל אני לא אגדיר את המושג הזה בפוסט, אז הנה אינטואיציה: בגזירה הראשונה, הצעד הראשון מפרק את הביטוי לשני חלקים - מה שמשמאל לפלוס ומה שלימינו. אם אנחנו מנסים לחשב את ערכו של הביטוי החשבוני, אפשר לחשוב שמעכשיו אנחנו מחשבים כל חלק בנפרד ובסוף נבצע חיבור שלהם. אגף שמאל יהיה שווה 1, ואגף ימין יהיה שווה {% equation %}2\times3=6{% endequation %}, ולכן הסכום ייתן 7. עד כאן, הגיוני; אבל אם נעשה את זה גם לגזירה השניה נראה שאחרי הצעד הראשון אנחנו מפרקים את הביטוי לאגף שמאל כפול אגף ימין, כאשר אגף ימין שווה ל-3 אבל אגף שמאל שווה ל-{% equation %}1+2=3{% endequation %} ולכן המכפלה צריכה לתת... תשע? לא הגיוני, כמובן - לנו זה נראה מובן מאליו שהביטוי שווה 7 כי אנחנו מניחים במובלע <strong>סדר קדימויות</strong> בין כפל וחיבור, אבל מבחינת הדקדוק זה לא קיים.

הסיטואציה הזו, שבה דקדוק יכול לגזור את אותה מילה בשתי דרכים שונות מהותית, היא בעייתית; לרוב משתמשים בנתונים על <strong>סדרת הגזירה</strong> של מילה בדקדוק מסויים כדי להבין את ה<strong>סמנטיקה</strong> שלו - מה הוא אומר בפועל (למשל, במקרה של ביטוי חשבוני, מה ערכו; אבל לעתים קרובות יותר, במקרה של תוכנית מחשב, מה היא עושה). שתי סדרות גזירה שונות פירושן שיש שתי דרכים שונות לפרש את המילה - בעיה. דקדוק שיש לו את הבעיה הזו - מילה אחת לפחות עם שתי סדרות גזירה שונות מהותית - נקרא דקדוק <strong>רב-משמעי</strong>. היינו שמחים, בהינתן הגדרה של דקדוק, לומר אם הוא רב משמעי - אבל באופן די מפתיע, גם זו בעיה לא כריעה אלגוריתמית, כי קל לראות שאם היא הייתה כריעה, גם PCP הייתה כריעה.

מה הרעיון? פשוט מאוד: נניח שיש לנו קלט לבעיית PCP, כלומר {% equation %}\left(a_{1},b_{1}\right),\dots,\left(a_{n},b_{n}\right){% endequation %}. אנחנו רוצים לבנות דקדוק שבו יש מילה שניתן לגזור בשתי דרכים שונות אם ורק אם אפשר להרכיב גם מה-{% equation %}a{% endequation %}-ים וגם מה-{% equation %}b{% endequation %}-ים את אותה מילה... די ברור מה צריך לעשות. פשוט נגדיר דקדוק שמשתניו הם {% equation %}S,A,B{% endequation %} עם כללי הגזירה {% equation %}S\to A|B{% endequation %} (הקו המפריד הזה אומר "או" - בעצם אני מתאר כאן שני כללי גזירה בו זמנית) וכמו כן {% equation %}A\to a_{i}A|a_{i}{% endequation %} ו-{% equation %}B\to b_{i}B|b_{i}{% endequation %} לכל {% equation %}1\le i\le n{% endequation %}.

למשל, עבור בעיית ה-PCP שהבאתי כדוגמה בתחילת הפוסט, עם הזוגות {% equation %}\left(00,0\right),\left(1,00\right),\left(0,10\right){% endequation %}, אקבל כללי גזירה כמו {% equation %}A\to00A{% endequation %} ו-{% equation %}A\to00{% endequation %} ו-{% equation %}B\to10{% endequation %} וכדומה. והנה שתי גזירות שונות של אותה מילה:

{% equation %}S\Rightarrow A\Rightarrow00A\Rightarrow0000A\Rightarrow00001A\Rightarrow000010{% endequation %}

{% equation %}S\Rightarrow B\Rightarrow0B\Rightarrow00B\Rightarrow0000B\Rightarrow000010{% endequation %}

זו בניה נחמדה מאוד, רק חבל שהיא לא עובדת. למה לא עובדת? מאותה סיבה שרוב הבניות הכושלות ברדוקציות בין בעיות חישוביות נכשלות - חשבנו רק על כיוון אחד של הבניה. מה שעשינו הוא לבדוק דקדוק שהוא על בטוח דו-משמעי אם בעיית ה-PCP המקורית פתירה; אבל ייתכן שהוא יהיה דו משמעי גם אם הבעיה המקורית אינה פתירה. למשל, תראו את הגזירות הללו עבור אותו דקדוק כמו קודם:

{% equation %}S\Rightarrow A\Rightarrow00{% endequation %}

{% equation %}S\Rightarrow B\Rightarrow00{% endequation %}

קל לבדוק ולוודא שאלו גזירות חוקיות בדקדוק, אבל 00 היא לא באמת מילה שיכולה להיווצר בבעיית ה-PCP בתור מילה משותפת, שכן היא מצריכה שימוש באינדקסים <strong>שונים</strong> עבור סדרות ה-{% equation %}a{% endequation %} וה-{% equation %}b{% endequation %} ({% equation %}a_{1}=00{% endequation %} אבל {% equation %}b_{2}=00{% endequation %}). לכן הדקדוק שלנו יצטרך בצורה כלשהי גם לציין מה היו האינדקסים שבהם הוא השתמש ביצירת המילה. התעלול הוא לפלוט אותם <strong>בסוף</strong> המילה. אז הנה מה שנעשה: נוסיף לטרמינלים שלנו סימבולים {% equation %}t_{1},\dots,t_{n}{% endequation %} ואת הסימבול {% equation %}\#{% endequation %} (שהוא מיותר אבל יעשה את מה שאעשה בהמשך טיפה יותר קריא) וכעת נבנה את הדקדוק הבא:

{% equation %}S\to A|B{% endequation %}

{% equation %}A\to a_{i}At_{i}|\#{% endequation %} לכל {% equation %}1\le i\le n{% endequation %}

{% equation %}B\to b_{i}Bt_{i}|\#{% endequation %}לכל {% equation %}1\le i\le n{% endequation %}

כעת אדגים שוב את הגזירות שנותנות את אותו הדבר:

{% equation %}S\Rightarrow A\Rightarrow00At_{1}\Rightarrow0000At_{1}t_{1}\Rightarrow00001At_{2}t_{1}t_{1}\Rightarrow000010At_{3}t_{2}t_{1}t_{1}\Rightarrow000010\#t_{3}t_{2}t_{1}t_{2}{% endequation %}

{% equation %}S\Rightarrow B\Rightarrow0Bt_{1}\Rightarrow00Bt_{1}t_{1}\Rightarrow0000Bt_{2}t_{1}t_{1}\Rightarrow000010Bt_{3}t_{2}t_{1}t_{1}\Rightarrow000010\#t_{3}t_{2}t_{1}t_{1}{% endequation %}

שימו לב שהאינדקסים מסודרים מהאחרון לראשון - קצת מחשבה תראה שלא יכלתי לעשות זאת בשום דרך אחרת. פרט לכך שזה נראה לנו, הקוראים, קצת מוזר, זה לא באמת מקלקל את ההוכחה.

עכשיו קל לראות שהגזירה השגויה שהצגתי למעלה, של 00, לא תעבוד:

{% equation %}S\Rightarrow A\Rightarrow00At_{1}\Rightarrow00\#t_{1}{% endequation %}

{% equation %}S\Rightarrow B\Rightarrow00Bt_{2}\Rightarrow00\#t_{2}{% endequation %}

כלומר, לא קיבלנו את אותה המילה כי {% equation %}t_{1}\ne t_{2}{% endequation %}. צריך עדיין לשבת ולהוכיח פורמלית שהרדוקציה עובדת, אבל היא עובדת. מסקנה: אם היינו יכולים לבדוק שדקדוק הוא רב משמעי, היינו יכולים לפתור את PCP, ולכן לא ניתן לבדוק את זה.

כמעט אותה בניה מראה לנו שעוד בעיה נפוצה עבור דקדוקים היא לא פתירה - נניח שיש לנו שני דקדוקים {% equation %}G_{1},G_{2}{% endequation %}, ואנחנו רוצים לבדוק שיש מילה ששניהם יודעים לייצר - כלומר, שהחיתוך של השפות שהם מייצרים הוא לא ריק. איך הבעיה הזו פותרת לנו את PCP? פשוט מאוד. במקום כללי הגזירה {% equation %}S\to A,S\to B{% endequation %} בדקדוק הקודם, פשוט נייצג שני דקדוקים ש-{% equation %}A{% endequation %} הוא המשתנה ההתחלתי של אחד מהם, ו-{% equation %}B{% endequation %} הוא המשתנה ההתחלתי של השני. באנג! עוד בעיה לא כריעה.

מספיק עם השימושים, בואו נעבור להוכחה ש-PCP לא כריעה. אבל לפני כן, אני אצטרך לעשות עוד תעלול טכני אחד ולעבור מ-PCP לבעיה כמעט זהה אבל עם מגבלה נוספת, שתקל עלי מאוד בהוכחה. המגבלה היא זו: עד כה, פתרון קביל ל-PCP יכל להשתמש בכל זוג מתי שבא לו. עכשיו אני רוצה להגביל את זה טיפ-טיפה: להגיד שהזוג <strong>הראשון</strong> שבו משתמשים יהיה זוג מיוחד, שמופיע רק פעם אחת - בהתחלה. במילים אחרות, הקלט לבעיה יהיה {% equation %}\left(a_{1},b_{1}\right),\dots,\left(a_{n},b_{n}\right){% endequation %} ובנוסף לכך עוד זוג {% equation %}\left(x,y\right){% endequation %}, והשאלה תהיה אם קיימת סדרת אינדקסים {% equation %}j,\dots,j_{k}{% endequation %} כך ש-{% equation %}xa_{j_{1}}a_{j_{2}}\cdots a_{j_{k}}=yb_{j_{1}}b_{j_{2}}\cdots b_{j_{k}}{% endequation %}. על הבעיה <strong>הזו</strong> יהיה לי הרבה יותר קל להראות שהיא לא כריעה; ולכן כדי להראות ש-PCP אינה כריעה, אני צריך קודם כל להסביר איך אני פותר את הבעיה החדשה בעזרת PCP.

התשובה היא שנעשה תעלול טכני. מתוך הקלט {% equation %}\left(x,y\right),\left(a_{1},b_{1}\right),\dots,\left(a_{n},b_{n}\right){% endequation %} אני הולך ליצור סדרה חדשה של זוגות, שמהונדסים בצורה ש"תכריח" את הזוג שמתאים ל-{% equation %}\left(x,y\right){% endequation %} להיות ראשון, למרות שחוקי המשחק לא מאפשרים לי להגדיר במפורש שאיבר כלשהו יהיה ראשון.

כרגיל, יהיה הכי נוח להסביר עם דוגמה, אז הנה קלט לדוגמה - וקלט ממש טיפשי, רק כדי שהמניפולציות שאעשה בהמשך יהיו ברורות. {% equation %}\left(x,y\right)=\left(11,1\right){% endequation %} ו-{% equation %}\left(a_{1},b_{1}\right)=\left(11,11\right){% endequation %}. ברור ש<strong>אין</strong> מילה משותפת, כי האורך של מילה שמתחילה ב-{% equation %}x{% endequation %} יהיה זוגי והאורך של מילה שמתחילה ב-{% equation %}y{% endequation %} יהיה אי זוגי, אבל אני לא יכול סתם לקחת את הזוגות הללו ולהתייחס אליהן כאל בעיית PCP רגילה, כי {% equation %}a_{1}=b_{1}{% endequation %} הוא פתרון לבעיית ה-PCP הרגילה (פשוט מתעלמים מה-{% equation %}\left(x,y\right){% endequation %}). אני חייב איכשהו להכריח את {% equation %}\left(x,y\right){% endequation %} להיות הזוג הראשון אם בכלל תהיה תקווה <strong>כלשהי</strong> לכך שנקבל מילה משותפת.

הרעיון הוא לדחוף סימן מיוחד - שוב פעם אשתמש ב-{% equation %}\#{% endequation %} - בין כל שתי אותיות, של כל מילה שמופיעה בכל זוג, אבל בצורה כזו שהמילה <strong>השמאלית</strong> בכל זוג <strong>תסתיים</strong> ב-{% equation %}\#{% endequation %}, ואילו המילה <strong>הימנית</strong> בכל זוג <strong>תתחיל</strong> ב-{% equation %}\#{% endequation %}. כלומר, אני אהפוך את הזוג {% equation %}\left(11,11\right){% endequation %} לזוג {% equation %}\left(1\#1\#,\#1\#1\right){% endequation %}. שימו לב לחוסר ההתאמה הזה במיקומי ה-{% equation %}\#{% endequation %}-ים; הוא מכוון.

כעת, גם ל-{% equation %}\left(x,y\right){% endequation %} אעניק טיפול דומה במובן זה שאדחוף להם {% equation %}\#{% endequation %} בין כל שתי אותיות, אבל <strong>אף אחד מהם </strong>לא יתחיל ב-{% equation %}\#{% endequation %}, ורק השמאלי יסתיים ב-{% equation %}\#{% endequation %}, כלומר, אני הופך את {% equation %}\left(11,1\right){% endequation %} ל-{% equation %}\left(1\#1\#,1\right){% endequation %}.

עכשיו, מה קורה פה? המילה {% equation %}xa_{1}{% endequation %}, שקודם הייתה {% equation %}1111{% endequation %}, הפכה עכשיו ל-{% equation %}1\#1\#1\#1\#{% endequation %}. המילה {% equation %}yb_{1}{% endequation %} הפכה ל-{% equation %}1\#1\#1{% endequation %}. כלומר - כל מילה שמורכבת מהמילים <strong>השמאליות</strong> בכל זוג הולכת להסתיים ב-{% equation %}\#{% endequation %}, וכל מילה שמורכבת מהמילים ה<strong>ימניות</strong> בכל זוג תסתיים בלי ה-{% equation %}\#{% endequation %} הזה. הדרך היחידה לקבל מילה זהה היא "לסגור" את הסיפור באמצעות עוד זוג מיוחד - הזוג {% equation %}\left(@,\#@\right){% endequation %} כאשר גם {% equation %}@{% endequation %} הוא תו מיוחד חדש שבו אני משתמש ולא מופיע במילים האחרות.

בואו נתאר פורמלית את מה שעשיתי. נגדיר אופרטור {% equation %}\Phi{% endequation %} שלוקח מילה {% equation %}w=\sigma_{1}\dots\sigma_{k}{% endequation %} ודוחף לה {% equation %}\#{% endequation %} בין כל האותיות, כלומר {% equation %}\Phi\left(w\right)=\sigma_{1}\#\sigma_{2}\dots\#\sigma_{k}{% endequation %}. כעת, אם קיבלנו בעיית PCP-עם-זוג-התחלתי {% equation %}\left(x,y\right),\left(a_{1},b_{1}\right),\dots,\left(a_{n},b_{n}\right){% endequation %} נייצר בעיית PCP "רגילה" עם הזוגות הבאים: לכל {% equation %}\left(a_{i},b_{i}\right){% endequation %} יהיה לנו את הזוג {% equation %}\left(\Phi\left(a_{i}\right)\#,\#\Phi\left(b_{i}\right)\right){% endequation %}. כמו כן, במקום {% equation %}\left(x,y\right){% endequation %} יהיה לנו {% equation %}\left(\Phi\left(x\right)\#,\Phi\left(y\right)\right){% endequation %}, וכמו כן יהיה לנו את הזוג הנוסף {% equation %}\left(@,\#@\right){% endequation %}. זה תרגיל מצויין לשבת ולהוכיח שזה עובד - שלבעיה המקורית היה פתרון אם ורק אם לבעיה החדשה עם ה-{% equation %}\#{% endequation %}-ים יש.

עכשיו אפשר להגיע סוף סוף לחלק המרכזי בפוסט - הוכחה שבעיית ה-PCP-עם-זוג-התחלתי היא לא כריעה. האופן שבו נעשה את זה הוא על ידי רדוקציה מהבעיה הלא כריעה הידועה ביותר במדעי המחשב - בעיית העצירה של מכונות טיורינג. לשם כך אזכיר בזריזות את מה שנצטרך לדעת על מכונות טיורינג (ו<a href="http://www.gadial.net/2007/09/23/turing_machine/">יש לי פוסט</a> על הנושא למי שמעוניין). אני הולך להציג כאן גרסה <strong>מפושטת</strong> של מכונות טיורינג ושל בעיית העצירה כי לא אצטרך יותר מכך - אל תסתכלו על מה שאכתוב עכשיו בתור ההגדרה האולטימטיבית!

מכונת טיורינג {% equation %}M{% endequation %} היא מעין מחשב קטן, עם קבוצת <strong>מצבים</strong> פנימיים סופית וסרט אינסופי בכיוון אחד (ימין) שמחולק לתאים שבכל אחד מהם כתובה אות כלשהי. יש למכונה ראש קורא/כותב שמתרוצץ על הסרט, קורא את תוכן התא שמעליו הוא נמצא כרגע, בודק באיזה מצב פנימי המכונה נמצאת, ועל פי הזוג הזה (המצב הפנימי והאות שקראנו) מחליט מה לעשות עכשיו - האם לשנות את תוכן התא, האם לשנות את המצב הפנימי של המכונה, והאם להזיז את הראש.

פורמלית מכונת טיורינג {% equation %}M{% endequation %} בנויה מקבוצת מצבים סופית {% equation %}Q{% endequation %}, מא"ב סופי כלשהו {% equation %}\Sigma{% endequation %} ומפונקציית מעברים {% equation %}\delta:Q\times\Sigma\to Q\times\Sigma\times\left\{ R,L,S\right\} {% endequation %}. {% equation %}\delta\left(q,\sigma\right)=\left(p,\tau,X\right){% endequation %} פירושו "אם היית במצב {% equation %}q{% endequation %} וקראת {% equation %}\sigma{% endequation %} עבור למצב {% equation %}p{% endequation %}, שנה את תוכן התא ל-{% equation %}\tau{% endequation %} והזז את הראש {% equation %}X{% endequation %}" כאשר אם {% equation %}X{% endequation %} הוא {% equation %}L{% endequation %} מזיזים את הראש צעד אחד שמאלה, אם הוא {% equation %}R{% endequation %} מזיזים אותו צעד אחד ימינה ואם הוא {% equation %}S{% endequation %} לא זזים. כמו כן למכונה יש מצב מיוחד {% equation %}q_{f}\in Q{% endequation %} שאם המכונה נכנסה אליו, אומרים שהיא "עצרה" ומפסיקים את החישוב שלה, ו-{% equation %}\delta{% endequation %} לא מוגדרת עליו (זה לא מתאים לכתיב הפורמלי שלי שבו {% equation %}\delta{% endequation %} מוגדרת על התחום {% equation %}Q\times\Sigma{% endequation %} אבל למי אכפת - אני מרשה לפונקציה הזו לא להיות מוגדרת על כל התחום שלה). יש גם סימן מיוחד {% equation %}\flat\in\Sigma{% endequation %} שמהווה את תוכן תאי הסרט כשהמכונה רק מתחילה לרוץ (חושבים עליו בתור "תא ריק") ומצב מיוחד {% equation %}q_{0}\in Q{% endequation %} שבו המכונה נמצאת כשהיא מתחילה לרוץ.

בעיה טכנית אחת שאולי שמתם לב אליה היא ש-{% equation %}M{% endequation %} עשויה להגיע אל הקצה השמאלי של הסרט, ואז לבצע עוד צעד שמאלה. לרוב מגדירים שבמקרה כזה, היא פשוט נשארת במקום; אבל זה יסבך את הבניה שאציג בהמשך. לכן אני הולך להניח שזה פשוט לא קורה. זה תרגיל נחמד - בהינתן מכונת טיורינג לבנות מכונה שקולה (עוצרת על אותם קלטים) שאף פעם לא "נופלת מקצה הסרט"; בפוסט הזה תאמינו לי שזה אפשרי.

כעת, בכל רגע נתון של הריצה שלה, הריצה של המכונה מאופיינת על ידי שלושה דברים: המצב הפנימי הנוכחי של המכונה; המיקום של הראש הקורא/כותב על גבי הסרט; ותוכן הסרט. שלושת אלו יחד נקראים <strong>הקונפיגורציה</strong> של המכונה. אפשר לכתוב קונפיגורציה בקיצור בצורה הבאה: סדרה של תווים שמתארת את תוכן תאי הסרט, כאשר התא שמעליו נמצא הראש הקורא/כותב אינו תו מתוך {% equation %}\Sigma{% endequation %} אלא תו מיוחד שהוא <strong>זוג</strong> של תו מתוך {% equation %}\Sigma{% endequation %} יחד עם תו שמתאר את המצב הפנימי הנוכחי של המכונה. למשל, {% equation %}ab\flat\left(q_{3},b\right)\flat a\flat{% endequation %} היא מחרוזת שמתארת את הקונפיגורציה הבאה: תוכן הסרט הוא {% equation %}ab\flat b\flat a\flat\flat\flat\dots{% endequation %}, המצב הפנימי הוא {% equation %}q_{3}{% endequation %} ומיקום הראש הוא מעל תא 4 (אם מתחילים את הספירה מ-1). שימו לב שקונפיגורציה מתוארת על ידי מחרוזת <strong>סופית</strong> למרות שהסרט הוא אינסופי - זאת מכיוון שאנחנו יודעים בודאות שכל תא שהמכונה טרם הגיעה אליו הוא ריק, ולכן אפשר להסכים שהמחרוזת מתארת רק את תוכן כל תאי הסרט שהמכונה הגיעה אליהם עד כה מתישהו במהלך ריצתה.

כעת, נניח שבמכונה שאת הקונפיגורציה שלה תיארתי לפני רגע יש את המעבר הבא: {% equation %}\delta\left(q_{3},b\right)=\left(q_{5},c,R\right){% endequation %}. אז מהקונפיגורציה {% equation %}ab\flat\left(q_{3},b\right)\flat a\flat{% endequation %} המכונה הולכת לעבור לקונפיגורציה {% equation %}ab\flat c\left(q_{5},\flat\right)a\flat{% endequation %}. ודאו לעצכם שאתם מבינים למה - זה יהיה <strong>קריטי לחלוטין</strong> בשביל מה שנעשה בהמשך להבין את כל הקטע המעיק הזה של מעבר קונפיגורציות (מעיק? למה מעיק? לדעתי זה נפלא, צורת התיאור הזו; אבל כל עוד לא רואים איך עושים איתה דברים מגניבים - כמו רדוקציה ל-PCP - זה נראה כמו משהו טכני יבשושי).

אם מקונפיגורציה א' מגיעים לקונפיגורציה ב' תוך צעד אחד, אומרים שב' היא <strong>עוקבת</strong> של א'. כמו כן, למכונה יש קונפיגורציה <strong>התחלתית</strong> פשוטה במיוחד - {% equation %}\left(q_{0},\flat\right){% endequation %} ("הסרט ריק, המצב הוא {% equation %}q_{0}{% endequation %}, הראש נמצא בתחילת הסרט"). קונפיגורציה <strong>סופית</strong> היא כל קונפיגורציה שבה המצב של המכונה הוא {% equation %}q_{f}{% endequation %}. בעיית העצירה היא בסך הכל השאלה הבאה - בהינתן מכונה {% equation %}M{% endequation %}, האם קיימת סדרת קונפיגורציות עוקבות שמתחילה בקונפיגורציה ההתחלתית ומסתיימת בקונפיגורציה סופית? והשאלה הזו, כאמור, אינה כריעה (לא ניכנס כעת להוכחה של הטענה הזו).

איך כל זה קשור ל-PCP? על פניו זה לא נראה כל כך קשור; אבל בואו ננסה לחשוב איך בכל זאת אפשר לקשר. ב-PCP השאלה היא האם קיימת "מילה משותפת" שאפשר לבנות בשתי דרכים שונות עם אותה סדרת אינדקסים; בבעיית העצירה השאלה היא האם קיימת "סדרת קונפיגורציות" שמתארת ריצה חוקית מקונפיגורציה התחלתית לקונפיגורציה סופית. אלו האובייקטים שעלינו לתרגם ביניהם - האם אפשר לתאר סדרת קונפיגורציות חוקית בתור מילה? בוודאי! כבר הראיתי איך לתאר קונפיגורציה בודדת בתור מילה, אז פשוט בואו נתקע איזה סימן {% equation %}\#{% endequation %} בין קונפיגורציות עוקבות! וכדי לפשט קצת יותר את העניינים, בואו ניפטר מהסוגריים המיותרים הללו שיש בתוך קונפיגורציה: במקום לכתוב {% equation %}ab\flat\left(q_{3},b\right)\flat a\flat{% endequation %} נכתוב {% equation %}ab\flat q_{3}b\flat a\flat{% endequation %} וכל עוד הסימבולים שמתארים מצבים והסימבולים שמתארים את הא"ב של המכונה הם שונים זה מזה לא תהיה בעיה של דו משמעות כאן.

הנה דוגמה לסדרת קונפיגורציות שכזו:

{% equation %}q_{0}\flat\#aq_{1}\flat\#q_{2}aa\#q_{f}aa{% endequation %}

אל תקראו רגע את ההמשך - שבו וכתבו במפורש אילו מעברים צריכים להיות במכונה כדי שתיתן את סדרת הקונפיגורציות הזו. רק כך נוכל להיות בטוחים שאתם מבינים את הפרטים הטכניים הרלוונטיים כאן - והפרטים הללו יהיו לב העניין אחר כך. כתבתם? יפה. המעברים הם {% equation %}\delta\left(q_{0},\flat\right)=\left(q_{1},a,R\right){% endequation %} ו-{% equation %}\delta\left(q_{1},\flat\right)=\left(q_{2},a,L\right){% endequation %} ו-{% equation %}\delta\left(q_{2},a\right)=\left(q_{f},a,S\right){% endequation %}.

עכשיו משהסכמנו על כך שהמילה המשותפת שנייצר תהיה סדרת קונפיגורציות שמתארת ריצה חוקית שעוצרת, נשאלת רק השאלה איך "לכפות" על המילה שנוצרת באמת לתאר ריצה כזו. לשם כך נצטרך להתבסס בצורה חזקה על הדרישה שיש לנו מ-PCP: שאותה סדרה תיווצר <strong>בשתי דרכים שונות</strong>, על ידי <strong>אותם אינדקסים</strong>. מה שנעשה הוא שניצור את המילה בצורה כזו שצד שמאל "רודף" כל הזמן אחרי צד ימין ומפגר אחריו בקונפיגורציה אחת בדיוק, וההזדמנות היחידה שלו להשיג את צד ימין ולהשלים את המילה היא אם צד ימין הגיע למצב הסופי {% equation %}q_{f}{% endequation %}. כדי לעשות את זה יותר ברור אני לא אצייר את המילים בתור צד שמאל וצד ימין אלא בתור למעלה ולמטה. בהתחלה שתי המילים שנבנות ייראו כך:

{% equation %}\begin{array}{cc}\#\\\# & q_{0}\flat\#\end{array}{% endequation %}

כעת, כדי שלמילה למעלה יהיה סיכוי "להדביק" את המילה שלמטה ועדיין להיות זהה לה, האותיות הבאות שחייבות להתווסף אליה הן {% equation %}q_{0}\flat{% endequation %}. עכשיו, נניח שלמכונה יש את הצעד הבא: {% equation %}\delta\left(q_{0},\flat\right)=\left(q_{1},a,R\right){% endequation %}. אנחנו רוצים שאחרי הוספת הזוג הבא, המילים שאנחנו בונים ייראו כך:

{% equation %}\begin{array}{ccc}\# & q_{0}\flat\\\# & q_{0}\flat & \#aq_{1}\end{array}{% endequation %}

כלומר, המילה שלמעלה "כיסתה" את החלק של {% equation %}q_{0}\flat{% endequation %} ואילצה את המילה שלמטה לבצע את המעבר שמקודד ב-{% equation %}\delta\left(q_{0},\flat\right){% endequation %}. איך נעשה את זה? פשוט מאוד: לרשימת הזוגות שלנו נוסיף את הזוג {% equation %}\left(q_{0}\flat,aq_{1}\right){% endequation %}. הוספת הזוג הזה למילה שנבנית יגרום בדיוק לתוצאה שאנחנו מעוניינים בה.

עכשיו צריך לטפל ב-{% equation %}\#{% endequation %} שמסמן סוף קונפיגורציה ומעבר לבאה בתור. אנחנו רוצים לסגור את הקונפיגורציה בו זמנית בשתי המילים, אז נשתמש בזוג {% equation %}\left(\#,\#\right){% endequation %} ונקבל:

{% equation %}\begin{array}{cccc}\# & q_{0}\flat & \#\\\# & q_{0}\flat & \# & aq_{1}\#\end{array}{% endequation %}

עכשיו, נניח שיש לנו את המעבר {% equation %}\delta\left(q_{1},\flat\right)=\left(q_{2},\flat,S\right){% endequation %}. איך נטפל בו? אנחנו אמורים להוסיף את הזוג {% equation %}\left(q_{1}\flat,q_{2}\flat\right){% endequation %} וזה בסדר גמור, אבל אם תשימו לב, במילה שלנו {% equation %}q_{1}{% endequation %} נמצא משמאל ל-{% equation %}\#{% endequation %} שמסמן את סוף הקונפיגורציה, ולא משמאל ל-{% equation %}\flat{% endequation %}. הרעיון הוא שהראש של המכונה הגיע אל הקצה של הסרט שכבר ראינו, ולכן במובלע נובע שיש שם {% equation %}\flat{% endequation %} אבל זה לא נכתב במפורש עדיין. איך נפתור את הבעיה הזו? פתרון מתבקש אחד הוא להוסיף מעבר מהצורה {% equation %}\left(q_{1}\#,q_{2}\flat\#\right){% endequation %} - אבל זה קצת מסורבל. אפשר להיות יותר חכמים ולמנוע את הבעיה מראש, כבר בשלב סגירת הקונפיגורציה: במקום להשתמש בזוג {% equation %}\left(\#,\#\right){% endequation %} אנחנו רוצים לאפשר גם להשתמש בזוג {% equation %}\left(\#,\flat\#\right){% endequation %} שאומר לקונפיגורציה למטה להוסיף {% equation %}\flat{% endequation %} כי אולי נזדקק לו תכף. אם היינו משתמשים בזוג הזה, זוג המילים שאנחנו בונים היה מהצורה:

{% equation %}\begin{array}{cccc}\# & q_{0}\flat & \#\\\# & q_{0}\flat & \# & aq_{1}\flat\#\end{array}{% endequation %}

וכעת אין בעיה; הזוג {% equation %}\left(q_{1}\flat,q_{2}\flat\right){% endequation %} מטפל בסיטואציה הנוכחית. האם סיימנו? לא, כי שימו לב ל-{% equation %}a{% endequation %} בתחילת הקונפיגורציה - זו האות הבאה שהמילה למעלה צריכה להוסיף לעצמה, וגם במילה למטה היא צריכה להופיע כי המכונה לא נוגעת בה בצעד הזה. אז נוסיף לנו זוג {% equation %}\left(a,a\right){% endequation %}, וכעת על ידי שימוש ב-{% equation %}\left(a,a\right){% endequation %} ואחריו ב-{% equation %}\left(q_{1}\flat,q_{2}\flat\right){% endequation %}, נקבל:

{% equation %}\begin{array}{ccccccc}\# & q_{0}\flat & \# & a & q_{1}\\\# & q_{0}\flat & \# & a & q_{1} & \# & aq_{2}\flat\end{array}{% endequation %}

לבסוף, נסגור את הקונפיגורציה בצורה "רגילה" עם {% equation %}\left(\#,\#\right){% endequation %} ונקבל:

{% equation %}\begin{array}{cccccc}\# & q_{0}\flat & \# & a & q_{1}\#\\\# & q_{0}\flat & \# & a & q_{1}\# & aq_{2}\flat\#\end{array}{% endequation %}

בואו נדבר עכשיו על תזוזה שמאלה של הראש, כלומר נניח שיש לנו את המעבר {% equation %}\delta\left(q_{2},\flat\right)=\left(q_{3},b,L\right){% endequation %}. מה קורה כאן? אנחנו רוצים לעבור לסיטואציה הבאה:

{% equation %}\begin{array}{cccccccc}\# & q_{0}\flat & \# & a & q_{1}\# & aq_{2}b\\\# & q_{0}\flat & \# & a & q_{1}\# & aq_{2}\flat & \# & q_{3}ab\end{array}{% endequation %}

כלומר, ב"מחיר" של הוספת {% equation %}aq_{2}b{% endequation %} למעלה אנחנו רוצים להוסיף {% equation %}q_{3}ab{% endequation %} למטה. לכן נוסיף את הזוג {% equation %}\left(aq_{2}b,q_{3}ab\right){% endequation %} לרשימת הזוגות שלנו.

רק דבר אחד עוד נותר לנו להבין לפני שנעבור לתיאור פורמלי של הכל - איך מסיימים? איך מאפשרים למילה שלמעלה להדביק את המילה שלמטה?

ובכן, בואו ניתן למכונה הבדיונית המסכנה שלי להגיע אל המנוחה והנחלה - נניח שיש לנו את המעבר {% equation %}\delta\left(q_{3},a\right)=\left(q_{f},a,S\right){% endequation %}. קודם כל, הוא יתבטא, כרגיל, בזוג {% equation %}\left(q_{3}a,q_{f}a\right){% endequation %} ונגיע אל הסיטואציה הבאה:

{% equation %}\begin{array}{ccccccccc}\# & q_{0}\flat & \# & a & q_{1}\# & aq_{2}b & \# & q_{3}a\\\# & q_{0}\flat & \# & a & q_{1}\# & aq_{2}\flat & \# & q_{3}a & b\#q_{f}a\end{array}{% endequation %}

המילה שלמעלה עדיין צריכה להדביק את ה-{% equation %}b\#{% endequation %} שלמטה עד שתגיע למצב שבו היא צריכה להשוות את ה-{% equation %}q_{f}{% endequation %} שלמטה; את זה היא תעשה עם הזוגות {% equation %}\left(b,b\right){% endequation %} ו-{% equation %}\left(\#,\#\right){% endequation %}, ואז נגיע למצב הבא:

{% equation %}\begin{array}{cccccccccc}\# & q_{0}\flat & \# & a & q_{1}\# & aq_{2}b & \# & q_{3}a & b\#\\\# & q_{0}\flat & \# & a & q_{1}\# & aq_{2}\flat & \# & q_{3}a & b\# & q_{f}ab\#\end{array}{% endequation %}

מה היינו <strong>רוצים</strong> שיקרה עכשיו? ובכן, היינו שמחים אם היה לנו את הזוג הבא: {% equation %}\left(q_{f}ab\#\#,\#\right){% endequation %}, שהיה משלים אותנו למילה המשותפת הבאה:

{% equation %}\begin{array}{cccccccccc}\# & q_{0}\flat & \# & a & q_{1}\# & aq_{2}b & \# & q_{3}a & b\# & q_{f}ab\#\#\\\# & q_{0}\flat & \# & a & q_{1}\# & aq_{2}\flat & \# & q_{3}a & b\# & q_{f}ab\#\#\end{array}{% endequation %}

למה לא להוסיף זוג כזה, באמת? למה לא להוסיף זוגות מהצורה {% equation %}\left(q_{f}w\#,\#\right){% endequation %} כאשר {% equation %}w{% endequation %} הוא המשך של קונפיגורציה עד ה-{% equation %}\#{% endequation %} שבסוף שלה, וזאת לכל {% equation %}w{% endequation %} אפשרית? תיאורטית, זה בדיוק מה שהיינו רוצים לעשות. מעשית, זה בלתי אפשרי כי יש <strong>אינסוף</strong> ערכים אפשריים של {% equation %}w{% endequation %}, אבל בעיית PCP תמיד מורכבת ממספר <strong>סופי</strong> של זוגות. אז יש לנו כאן מגבלה טכנית קלה, ולכן יהיה לה פתרון טכני קל. במקום "לאכול" את כל הקונפיגורציה בבת אחת, נאכל אותה תו תו.

מה זה אומר? זה אומר שנתחיל עם הזוג {% equation %}\left(q_{f}a,q_{f}\right){% endequation %}, ואחרי שנשתמש בו נגיע לסיטואציה הבאה:

{% equation %}\begin{array}{ccccccccccc}\# & q_{0}\flat & \# & a & q_{1}\# & aq_{2}b & \# & q_{3}a & b\# & q_{f}a\\\# & q_{0}\flat & \# & a & q_{1}\# & aq_{2}\flat & \# & q_{3}a & b\# & q_{f}a & b\#q_{f}\end{array}{% endequation %}

עכשיו נעתיק את שארית הקונפיגורציה עד לפעם הבאה שבה המילה שלמעלה תצטרך לכתוב {% equation %}q_{f}{% endequation %}, ונגיע לדבר הבא:

{% equation %}\begin{array}{cccccccccccc}\# & q_{0}\flat & \# & a & q_{1}\# & aq_{2}b & \# & q_{3}a & b\# & q_{f}a & b\#\\\# & q_{0}\flat & \# & a & q_{1}\# & aq_{2}\flat & \# & q_{3}a & b\# & q_{f}a & b\# & q_{f}b\#\end{array}{% endequation %}

מה קרה פה? אם נקרא רק את המילה למטה, זה נראה כאילו עברנו מהקונפיגורציה {% equation %}q_{f}ab{% endequation %} לקונפיגורציה {% equation %}q_{f}b{% endequation %} - כאילו ה-{% equation %}a{% endequation %} "נאכל" על ידי {% equation %}q_{f}{% endequation %}. זה בדיוק מה שהולך לקרות - {% equation %}q_{f}{% endequation %} הרעבתן הולך לבלוס את כל המילה שנמצאת מימינו בקונפיגורציה, אות אחרי אות. ומתי נוכל לסיים? כשיגיע הזמן לבלוס את ה-{% equation %}\#{% endequation %} שבסוף. כלומר, כשנגיע למצב הבא:

{% equation %}\begin{array}{cccccccccccccc}\# & q_{0}\flat & \# & a & q_{1}\# & aq_{2}b & \# & q_{3}a & b\# & q_{f}a & b\# & q_{f}b & \#\\\# & q_{0}\flat & \# & a & q_{1}\# & aq_{2}\flat & \# & q_{3}a & b\# & q_{f}a & b\# & q_{f}b & \# & q_{f}\#\end{array}{% endequation %}

את זה אפשר לסיים על ידי הזוג {% equation %}\left(q_{f}\#\#,\#\right){% endequation %}, מה שיביא אותנו אל

{% equation %}\begin{array}{cccccccccccccc}\# & q_{0}\flat & \# & a & q_{1}\# & aq_{2}b & \# & q_{3}a & b\# & q_{f}a & b\# & q_{f}b & \# & q_{f}\#\#\\\# & q_{0}\flat & \# & a & q_{1}\# & aq_{2}\flat & \# & q_{3}a & b\# & q_{f}a & b\# & q_{f}b & \# & q_{f}\#\#\end{array}{% endequation %}

וסיימנו!

יש עוד נקודה עדינה שצריך להתייחס אליה - {% equation %}q_{f}{% endequation %} יצטרך לאכול גם סימנים שמשמאלו בקונפיגורציה אם יש כאלו. כדי לראות את זה, בואו נתחיל דוגמה חדשה:

{% equation %}\begin{array}{cc}\#q_{0}\flat\#\\\#q_{0}\flat\# & aq_{f}\#\end{array}{% endequation %}

מה עכשיו? כדי להשוות את ה-{% equation %}a{% endequation %} שיש למטה, חייבים להשתמש בזוג {% equation %}\left(a,a\right){% endequation %}, ואז נגיע לסיטואציה הבאה:

{% equation %}\begin{array}{ccc}\#q_{0}\flat\# & a\\\#q_{0}\flat\# & a & q_{f}\#a\end{array}{% endequation %}

אבל עכשיו אם נשתמש בזוג {% equation %}\left(q_{f}\#\#,\#\right){% endequation %}, מה שנגיע אליו יהיה

{% equation %}\begin{array}{cccc}\#q_{0}\flat\# & a & q_{f}\#\#\\\#q_{0}\flat\# & a & q_{f}\#a & \#\end{array}{% endequation %}

ויש לנו כאן בבירור אי התאמה. לכן אין מנוס - נצטרך "לאכול" את ה-{% equation %}a{% endequation %} עם זוג מהצורה {% equation %}\left(aq_{f},q_{f}\right){% endequation %}. יחד איתנו נגיע ישירות מהמצב הבא:

{% equation %}\begin{array}{cc}\#q_{0}\flat\#\\\#q_{0}\flat\# & aq_{f}\#\end{array}{% endequation %}

אל המצב הזה:

{% equation %}\begin{array}{ccc}\#q_{0}\flat\# & aq_{f}\\\#q_{0}\flat\# & aq_{f} & \#q_{f}\end{array}{% endequation %}

ומכאן נגיע אל

{% equation %}\begin{array}{cccc}\#q_{0}\flat\# & aq_{f} & \#\\\#q_{0}\flat\# & aq_{f} & \# & q_{f}\#\end{array}{% endequation %}

ומפה כבר נסתדר. ועכשיו זה באמת מסיים את כל הפינות האפלות של הבניה (תוך שימוש מובלע בהנחות שציינתי קודם, למשל שהמכונה אף פעם לא מנסה לפנות שמאלה כשהיא בקצה השמאלי של הסרט).

כל זה היה הסבר אינטואיטיבי, אבל לדעתי זה העיקר כאן. אחרי שהבנו אותו, כל מה שנשאר הוא ההגדרה היבשה. בהינתן מ"ט {% equation %}M{% endequation %}, אנחנו בונים ממנה בעיית PCP עם זוג התחלתי באופן הבא:
<ul>
	<li>הזוג ההתחלתי יהיה {% equation %}\left(\#,\#q_{0}\flat\#\right){% endequation %}.</li>
	<li>לכל {% equation %}a\in\Sigma{% endequation %} יהיה לנו הזוג {% equation %}\left(a,a\right){% endequation %}</li>
	<li>יהיו לנו הזוגות {% equation %}\left(\#,\#\right){% endequation %} ו-{% equation %}\left(\#,\flat\#\right){% endequation %}.</li>
	<li>לכל מעבר {% equation %}\delta\left(q,\sigma\right)=\left(p,\tau,R\right){% endequation %} יהיה לנו הזוג {% equation %}\left(q\sigma,\tau p\right){% endequation %}.</li>
	<li>לכל מעבר {% equation %}\delta\left(q,\sigma\right)=\left(p,\tau,S\right){% endequation %} יהיה לנו הזוג {% equation %}\left(q\sigma,p\tau\right){% endequation %}.</li>
	<li>לכל מעבר {% equation %}\delta\left(q,\sigma\right)=\left(p,\tau,L\right){% endequation %} ולכל {% equation %}a\in\Sigma{% endequation %} יהיה לנו הזוג {% equation %}\left(aq\sigma,pa\tau\right){% endequation %}.</li>
	<li>לכל {% equation %}a\in\Sigma{% endequation %} יהיו לנו הזוגות {% equation %}\left(q_{f}a,q_{f}\right){% endequation %} ו-{% equation %}\left(aq_{f},q_{f}\right){% endequation %}.</li>
	<li>יהיה לנו הזוג {% equation %}\left(q_{f}\#\#,\#\right){% endequation %}.</li>
</ul>
וזו הבניה כולה! קלה, אחרי שמבינים את הרעיון. האם הצלחתי להסביר את הרעיון?

