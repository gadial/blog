---
id: 1296
title: "תורת המספרים האלגברית על קצה המזלג, חלק ג' - שובו של הפירוק היחיד"
date: 2011-08-23 11:48:07
layout: post
categories: 
  - אלגברה מופשטת
  - תורת המספרים
tags: 
  - גם טכני זה כיף!
  - הוכחות
  - חוגי דדקינד
  - תורת המספרים האלגברית
---
בפוסט הקודם הצגתי את הפתרון של דדקינד (שהלך בעקבות קומר) לבעיה של אי-פריקות יחידה בחוגי שלמים. הרעיון היה לעבור מדיבור על אברי החוג לדיבור על <strong>אידאלים</strong> של החוג - כשאידאל הייתה קבוצה של אברי החוג שסגורה לחיבור ו"בולעת" כפל באיבר כלשהו מהחוג. פורמלית, אם {% equation %}R{% endequation %} הוא חוג אז {% equation %}I{% endequation %} הוא אידאל אם לכל {% equation %}x,y\in I{% endequation %} מתקיים {% equation %}x+y\in I{% endequation %} (למעשה, צריך לדרוש באופן כללי שיתקיים דווקא {% equation %}x-y\in I{% endequation %} שכן גם סגירות לחיסור חשובה וממנה נובעת סגירות לחיבור, אבל במקרה שלנו זה נובע מתכונת הבליעה) ולכל {% equation %}r\in R{% endequation %} מתקיים ש-{% equation %}xr\in I{% endequation %}.

הגדרנו גם פעולות על האידאלים. כפל הוגדר על ידי {% equation %}AB=\left\{ \sum_{i=1}^{n}a_{i}b_{i}|a_{i}\in A,b_{i}\in B,n\in\mathbb{N}\right\} {% endequation %}, חיבור הוגדר על ידי {% equation %}A+B=\left\{ a+b|a\in A,b\in B\right\} {% endequation %} וראינו כי כאשר חושבים על {% equation %}A,B{% endequation %} בתור מעין מספרים הפעולה הזו מתאימה לא לחיבור מספרים אלא ללקיחת המחלק המשותף המקסימלי שלהם. לסיום דיברנו על אידאלים ראשוניים ומקסימליים - הכללות של המושגים של ראשוניות ואי-פריקות של איברי החוג, והזכרתי שבחוגי שלמים מתקיימת התופעה הנחמדה שבה כל אידאל ראשוני הוא גם מקסימלי, וציינתי שזו אחת מבין שלוש תכונות שמבטיחות שבחוג תהיה פריקות יחידה לאידאלים. עכשיו אני רוצה לתאר את שתי התכונות האחרות - החוג צריך להיות נתרי, והוא צריך להיות סגור בשלמים.

אינטואיטיבית, חוג נתרי הוא חוג שבו תהליך חלוקה של מספר חייב להסתיים מתישהו. פורמלית התכונה מנוסחת כך: {% equation %}R{% endequation %} הוא נתרי אם לכל סדרה של אידאלים ב-{% equation %}R{% endequation %} שמקיימת {% equation %}I_{1}\subseteq I_{2}\subseteq I_{3}\subseteq\dots{% endequation %} הסדרה "נעצרת" מתישהו, במובן זה שקיים {% equation %}n{% endequation %} כך ש-{% equation %}I_{n}=I_{n+1}=I_{n+2}=\dots{% endequation %} וכן הלאה.

כדי להבין את התכונה הזו כדאי להיזכר שוב בכך שאם {% equation %}A,B{% endequation %} אידאלים כך ש-{% equation %}A\subseteq B{% endequation %}, אנחנו חושבים על כך כאילו ה"מספר" {% equation %}B{% endequation %} מחלק את ה"מספר" {% equation %}A{% endequation %}. כדי להקל על הדמיון אנחנו משתמשים בסימונים כמו {% equation %}\mathfrak{a}{% endequation %} ו-{% equation %}\mathfrak{b}{% endequation %} לאידאלים (סימנים שיותר נראים כמו מספרים - מוזרים - מאשר קבוצות) ומשתמשים בסימון כמו {% equation %}\mathfrak{b}|\mathfrak{a}{% endequation %} כדי לציין בדיוק את זה ש-{% equation %}\mathfrak{a}\subseteq\mathfrak{b}{% endequation %}. נתריות של חוג אומרת שלא קיימת סדרה {% equation %}\mathfrak{a}_{1},\mathfrak{a}_{2},\mathfrak{a}_{3},\dots{% endequation %} שבה כל איבר מחלק את קודמו ({% equation %}\mathfrak{a}_{2}|\mathfrak{a}_{1}{% endequation %}, {% equation %}\mathfrak{a}_{3}|\mathfrak{a}_{1}{% endequation %} וכן הלאה) ואינה עוצרת אף פעם. בואו נסתכל על דוגמה קונקרטית מתוך {% equation %}\mathbb{Z}{% endequation %} - למשל, האידאל {% equation %}\left(60\right){% endequation %}. מי מכיל אותו? למשל, {% equation %}\left(30\right){% endequation %}. ומי מכיל אותו? למשל, {% equation %}\left(15\right){% endequation %}. ואותו? למשל, {% equation %}\left(3\right){% endequation %}. ואותו? הממ, אותו מכיל רק {% equation %}\left(1\right){% endequation %}. ומי מכיל את {% equation %}\left(1\right){% endequation %}? אהה... מכיוון ש-{% equation %}\left(1\right)=\mathbb{Z}{% endequation %}, אז האידאל היחיד שמכיל אותו זה הוא עצמו. קיבלנו את הסדרה {% equation %}\left(60\right)\subseteq\left(30\right)\subseteq\left(15\right)\subseteq\left(3\right)\subseteq\left(1\right)\subseteq\left(1\right)\subseteq\left(1\right)\subseteq\dots{% endequation %}.

חייבים להודות שזו תכונה טבעית למדי והכרחית כדי שנוכל בכלל לדבר על פירוק לאידאלים; שהרי אחרת קיימת הסכנה שנתחיל לפרק אידאל כלשהו, ונפרק ונפרק ונפרק וזה לעולם לא יסתיים.

התכונה השלישית היא סגירות בשלמים. אמרנו שאם {% equation %}K{% endequation %} היא הרחבה אלגברית סופית של הרציונליים, אז {% equation %}\mathcal{O}_{K}{% endequation %} היא בדיוק אותם מספרים ב-{% equation %}K{% endequation %} שמאפסים פולינום מתוקן עם מקדמים <strong>שלמים</strong>. צריך לחשוב על זה כאילו לקחנו את {% equation %}\mathbb{Z}{% endequation %} והרחבנו אותו, באופן דומה לזה שבו הרחבנו את {% equation %}\mathbb{Q}{% endequation %} כדי לקבל את {% equation %}K{% endequation %}. כעת אפשר לדבר על פולינום עם מקדמים "שלמים פלוס פלוס" - מקדמים מתוך {% equation %}\mathcal{O}_{K}{% endequation %}. האם יש איברים "חדשים" ב-{% equation %}K{% endequation %} שמאפסים פולינומים מתוקנים עם מקדמים מתוך {% equation %}\mathcal{O}_{K}{% endequation %}, או שב-{% equation %}\mathcal{O}_{K}{% endequation %} יש כבר את כל המספרים שעושים זאת? התשובה היא שב-{% equation %}\mathcal{O}_{K}{% endequation %} יש את כל האיברים שעושים זאת. הדבר דומה לסגירות האלגברית של {% equation %}\mathbb{C}{% endequation %} - העובדה שכל פולינום עם מקדמים מרוכבים מאופס רק על ידי מספרים מרוכבים, ולא צריך להרחיב עוד את מערכת המספרים המרוכבים רק שכעת אנו מדברים במפורש על פולינומים מתוקנים. הערה קטנה למתקדמים: באופן כללי עבור חוג {% equation %}R{% endequation %}, ה-{% equation %}K{% endequation %} הרלוונטי לצורך דיבורים על סגירות בשלמות הוא שדה השברים שלו; כאשר עוסקים בשדות מספרים אפשר להראות ששדה השברים של {% equation %}\mathcal{O}_{K}{% endequation %} הוא אכן {% equation %}K{% endequation %}.

שלוש התכונות הללו של חוג - נתרי, סגור בשלמים וכל אידאל ראשוני בו הוא מקסימלי - הן שלוש התכונות שנדרשות כדי לקבל פריקות יחידה של אידאלים. הם מתקיימות על ידי {% equation %}\mathcal{O}_{K}{% endequation %}, אבל גם על ידי חוגים אחרים, כלליים יותר. ראשית, החוגים שאנחנו מדברים עליהם חייבים להיות תחומי שלמות קומוטטיביים עם יחידה: "תחום שלמות" פירושו שאם מכפלה של שני איברים היא אפס, אחד מהם הוא אפס (בלי התכונה הזו אי אפשר לדבר על שדה השברים של החוג), "קומוטטיבי" אומר ש-{% equation %}ab=ba{% endequation %} לכל שני איברים בחוג (זה לא נכון, למשל, עבור חוגי מטריצות) ועם יחידה אומר שקיים איבר שמסומן ב-{% equation %}1{% endequation %} כך ש-{% equation %}a\cdot1=1\cdot a=a{% endequation %} לכל איבר בחוג. התכונות הללו מובנות מאליהן בחוגי שלמים אבל לא בחוגים כלליים יותר.

חוגים שבנוסף לדרישות הסטנדרטיות הללו מקיימים את שלוש התכונות שלעיל (נתרי, סגור, ראשוני-מקסימלי) נקראים <strong>חוגי דדקינד</strong>. הנקודה שבה חוגי שלמים הם "מעניינים יותר" מחוגי דדקינד כלליים היא לא בפריקות היחידה אלא בתכונה אחרת שקשורה למשהו שנקרא "מספר המחלקה" (Class Number) שאתאר בהמשך.

סיימנו את ההקדמה. עכשיו נשאלות שתי שאלות באופן טבעי - ראשית, למה כל חוג שלמים הוא חוג דדקינד? שנית, למה בחוג דדקינד יש פריקות יחידה לאידאלים? ההוכחות לדברים הללו אינן טריוויאליות ודורשות ידע מוקדם כלשהו במתמטיקה; אנסה לתת סקיצות שיבהירו את רוח הדברים גם אם לא יהוו הוכחות מדויקות. נתחיל דווקא מלראות מדוע חוג דדקינד הוא בעל פריקות יחידה; אחרי שרואים למה התכונות הדדיקנדיות עוזרות לנו, יש קצת יותר סבלנות להבין מדוע הן נכונות.

ההוכחה עצמה תהיה דומה מאוד באופיה להוכחה ה"קלאסית" לכך שב-{% equation %}\mathbb{Z}{% endequation %} יש פריקות יחידה ("המשפט היסודי של האריתמטיקה"), ולכן אציג קודם כל את ההוכחה הזו. אנחנו צריכים להוכיח שני דברים: שלכל מספר {% equation %}a\in\mathbb{N}{% endequation %} כך ש-{% equation %}a\ne0,1{% endequation %} <strong>קיים</strong> פירוק למכפלה של מספרים ראשוניים חיוביים {% equation %}a=p_{1}\cdot p_{2}\dots p_{k}{% endequation %} (אותו ראשוני עשוי להופיע כמה פעמים במכפלה), ושהפירוק הזה הוא <strong>יחיד</strong> עד כדי סדר האיברים במכפלה. שימו לב לכך שיש לנו כאן שני דברים שצריך להוכיח - זו דוגמה קלאסית למשפט קיום ויחידות (דבר נפוץ למדי במתמטיקה).

נתחיל מקיום. מכיוון שאני רוצה לתת הוכחה שתהיה דומה באופיה להוכחה עבור אידאלים בהמשך, מה שאעשה ייראה אולי טיפה מוזר במבט ראשון. אני מניח בשלילה שלא כל המספרים הטבעיים הגדולים מ-1 ניתנים להצגה כמכפלה של ראשוניים, ובוחר את {% equation %}a{% endequation %} להיות <strong>המינימלי</strong> מביניהם. לא ייתכן שהוא עצמו ראשוני, שהרי אז הוא כן היה ניתן להצגה כמכפלה של ראשוניים (המכפלה {% equation %}a{% endequation %}). מה שאני כן יודע הוא שקיים ראשוני {% equation %}p&lt;a{% endequation %} כך ש-{% equation %}p|a{% endequation %} (זו טענה שצריך להוכיח, כמובן; כשאדבר על אידאלים גם אסביר איך מוכיחים אותה במקרה הכללי יותר הזה). אם נחלק את {% equation %}a{% endequation %} ב-{% equation %}p{% endequation %}, נקבל את המספר {% equation %}ap^{-1}{% endequation %} שהוא עדיין מספר טבעי, אבל קטן מ-{% equation %}a{% endequation %}; אם הוא קטן מ-{% equation %}a{% endequation %}, אז על פי המינימליות של {% equation %}a{% endequation %}, את {% equation %}ap^{-1}{% endequation %} בהכרח אפשר לתאר כמכפלה של ראשוניים: {% equation %}ap^{-1}=p_{1}\cdots p_{k}{% endequation %}. נכפול את שני האגפים ב-{% equation %}p{% endequation %} ונקבל: {% equation %}a=pp_{1}\cdots p_{k}{% endequation %} וסיימנו (קיבלנו סתירה לכך ש-{% equation %}a{% endequation %} לא ניתן להצגה כמכפלת ראשוניים ולכן אין מספרים שלא ניתנים להצגה כזו).

כעת נעבור להוכיח יחידות. יהא {% equation %}a{% endequation %} מספר טבעי גדול מ-1 כלשהו כך ש-{% equation %}a=p_{1}\cdots p_{k}{% endequation %} וגם {% equation %}a=q_{1}\cdots q_{t}{% endequation %} כשכל האיברים במכפלות הם ראשוניים. הבה ונתבונן ב-{% equation %}p_{1}{% endequation %}: הוא מחלק את {% equation %}a{% endequation %} ולכן את {% equation %}q_{1}\cdots q_{t}{% endequation %}. כזכור, לראשוני יש את התכונה המופלאה שאם הוא מחלק מכפלה הוא מחלק אחד מהמוכפלים (הגדרתי זאת עבור שני מוכפלים; קל להראות שזה נכון עבור מספר סופי כלשהו של מוכפלים). לכן קיים {% equation %}q_{i}{% endequation %} כך ש-{% equation %}p_{1}|q_{i}{% endequation %}. אבל {% equation %}q_{i}{% endequation %} הוא ראשוני ולכן אם הוא מתחלק ב-{% equation %}p_{1}{% endequation %} (שהוא בתורו גדול מ-1), הם חייבים להיות שווים - {% equation %}p_{1}=q_{i}{% endequation %}. כעת נכפול את שני אגפי המשוואה {% equation %}p_{1}\cdots p_{k}=q_{1}\cdots q_{t}{% endequation %} ב-{% equation %}p_{1}^{-1}{% endequation %} ונקבל ש-{% equation %}p_{2}\cdots p_{k}=q_{1}\cdots q_{i-1}q_{i+1}\cdots q_{t}{% endequation %}, ואת התהליך הזה ניתן להמשיך באינדוקציה (על מספר האיברים במכפלה) ולקבל בסופו של דבר שכולם שווים עד כדי שינוי סדר.

אני מקווה שההוכחה הזו הייתה פשוטה דיו כדי שכל קוראי הפוסט יבינו אותה; אם הבנתם אותה, הבנתם גם את ההוכחה על פירוק יחיד לאידאלים ורק נותר לגהץ קצת את הפרטים.

החלק היחיד בכל מה שעשיתי שלא עובר בצורה פשוטה ומיידית לאידאלים הוא ההכפלה ב-{% equation %}p^{-1}{% endequation %} שאני מבצע גם בהוכחת הקיום וגם בהוכחת היחידות. אם תתבוננו היטב בהוכחה, תראו שאני משתמש ב-{% equation %}p^{-1}{% endequation %} בשתי דרכים שונות: גם בטענה ש-{% equation %}p^{-1}a{% endequation %} קטן יותר מ-{% equation %}a{% endequation %}, וגם בכך ש-{% equation %}p^{-1}p=1{% endequation %}, כך שאפשר "לבטל" את {% equation %}p{% endequation %} מהמשוואה על ידי כפל ב-{% equation %}p^{-1}{% endequation %}. ברור שכשעוברים לאידאלים צריך להגדיר בחוכמה את האנלוג של {% equation %}p^{-1}{% endequation %} כדי שיקיים תכונות אלו; וההוכחה שהאנלוג אכן עובד היא עיקר הסיבוך הטכני שלנו כאן.

נעבור כעת לדבר על חוגי דדקינד כלליים. {% equation %}\mathcal{O}{% endequation %} יהיה חוג דדקינד - תחום שלמות שהוא נתרי, סגור בשלמות וכל אידאל ראשוני בו הוא מקסימלי. ב-{% equation %}K{% endequation %} אסמן את שדה השברים של {% equation %}\mathcal{O}{% endequation %} - אוסף כל האיברים מהצורה {% equation %}\frac{a}{b}{% endequation %} כאשר {% equation %}a,b\in\mathcal{O}{% endequation %} ו-{% equation %}b\ne0{% endequation %}, עם כללי החיבור והכפל הרגילים עבור שברים והכלל ש-{% equation %}\frac{a}{b}=\frac{c}{d}{% endequation %} אם {% equation %}ad=bc{% endequation %}. בהינתן אידאל ראשוני {% equation %}\mathfrak{p}{% endequation %} של {% equation %}\mathcal{O}{% endequation %}, נסמן ב-{% equation %}\mathfrak{p}^{-1}{% endequation %} את הקבוצה הבאה: {% equation %}\mathfrak{p}^{-1}=\left\{ x\in K|x\mathfrak{p}\subseteq\mathcal{O}\right\} {% endequation %}. במילים - {% equation %}\mathfrak{p}^{-1}{% endequation %} כולל את כל אברי שדה השברים של {% equation %}\mathcal{O}{% endequation %} שכל איבר באידאל {% equation %}\mathfrak{p}{% endequation %} "מצמצם להם את המכנה" - כשכופלים אותם בכל אברי {% equation %}\mathfrak{p}{% endequation %} תמיד מקבלים שלם. למשל, אם {% equation %}\mathfrak{p}=\left(3\right){% endequation %} בחוג {% equation %}\mathbb{Z}{% endequation %}, נקבל ש-{% equation %}\mathfrak{p}^{-1}{% endequation %} כולל את כל השלמים (באופן כללי {% equation %}\mathfrak{p}^{-1}{% endequation %} תמיד כולל את כל {% equation %}\mathcal{O}{% endequation %}, ישירות מההגדרה) אבל גם כולל את {% equation %}\frac{1}{3}{% endequation %}. שימו לב שזה כלל לא אידאל של {% equation %}\mathcal{O}{% endequation %} - הוא כולל איברים שלא בהכרח נמצאים ב-{% equation %}\mathcal{O}{% endequation %}.

התוצאה החשובה על {% equation %}\mathfrak{p}^{-1}{% endequation %}, לצרכנו, היא ש-{% equation %}\mathfrak{a}\cdot\mathfrak{p}^{-1}\ne\mathfrak{a}{% endequation %} לכל אידאל {% equation %}\mathfrak{a}\ne0{% endequation %}, כאשר כפל מוגדר בדיוק כמו כפל של אידאלים (סכומים סופיים של מכפלות). לא אוכיח את התוצאה הזו כרגע; לב לבה הטכני של ההוכחה טמון בה ואני מעדיף לדחות את זה לסוף. זה המקום שבו משתמשים בכך ש-{% equation %}\mathcal{O}{% endequation %} הוא סגור בשלמים. בינתיים בואו ננסה להבין טיפה את המסקנות ממנה.

ראשית, מכיוון ש-{% equation %}\mathcal{O}\subseteq\mathfrak{p}^{-1}{% endequation %} נקבל ש-{% equation %}\mathfrak{a}\subset\mathfrak{a}\cdot\mathfrak{p}^{-1}{% endequation %} (למה?). שנית, באופן כללי {% equation %}\mathfrak{a}\cdot\mathfrak{p}^{-1}{% endequation %} לא חייב להיות אידאל (ייתכן שיהיו בו איברים שאינם ב-{% equation %}\mathcal{O}{% endequation %}) אבל אם {% equation %}\mathfrak{a}\subseteq\mathfrak{p}{% endequation %}, אז {% equation %}\mathfrak{a}\cdot\mathfrak{p}^{-1}{% endequation %} אכן יהיה אידאל (בדוק זאת!)

שלישית, במקרה שבו {% equation %}\mathfrak{a}=\mathfrak{p}{% endequation %} נקבל מהתוצאה לעיל ש-{% equation %}\mathfrak{p}\subset\mathfrak{p}\cdot\mathfrak{p}^{-1}\subseteq\mathcal{O}{% endequation %}; אבל {% equation %}\mathfrak{p}{% endequation %} הוא אידאל ראשוני ולכן מקסימלי (כי {% equation %}\mathcal{O}{% endequation %} הוא חוג דדקינד) ולכן מהגדרת המקסימליות של אידאלים נובע ש-{% equation %}\mathfrak{p}\cdot\mathfrak{p}^{-1}=\mathcal{O}{% endequation %} - אז במובן כלשהו זהו אכן ההופכי, והוא אכן מקיים את תכונת ה"הקטנה" של {% equation %}\mathfrak{a}{% endequation %} שרצינו ({% equation %}\mathfrak{a}\subset\mathfrak{a}\mathfrak{p}^{-1}{% endequation %} משמעו ש-{% equation %}\mathfrak{a}\mathfrak{p}^{-1}{% endequation %} מחלק ממש את {% equation %}\mathfrak{a}{% endequation %}).

עוד דבר שאזדקק לו הוא האבחנה שאם {% equation %}\mathfrak{p}{% endequation %} הוא אידאל ראשוני שמחלק מכפלה כלשהי של אידאלים {% equation %}\mathfrak{a}_{1}\cdots\mathfrak{a}_{k}{% endequation %} אז הוא מחלק את אחד מאבריה, בדיוק כמו שקורה עם מספרים שלמים. ההוכחה לכך פשוטה ואלגנטית: נניח ש-{% equation %}\mathfrak{p}{% endequation %} לא מחלק אף אחד מאברי המכפלה, כלומר הוא לא מכיל אף אחד מהאידאלים {% equation %}\mathfrak{a}_{1},\cdots,\mathfrak{a}_{k}{% endequation %}; אז קיימים {% equation %}a_{1},\dots,a_{k}\in\mathcal{O}{% endequation %} השייכים לאידאלים המתאימים כך ש-{% equation %}a_{1},\dots,a_{k}\notin\mathfrak{p}{% endequation %}. אבל מכפלתם שייכת ל-{% equation %}\mathfrak{a}_{1}\cdots\mathfrak{a}_{k}{% endequation %} ולכן שייכת ל-{% equation %}\mathfrak{p}{% endequation %}, ומהגדרתו של אידאל ראשוני עולה שאחד מאבריה צריך להיות שייך ל-{% equation %}\mathfrak{p}{% endequation %}. באופן הזה תכונת ה"אם ראשוני מחלק מכפלה הוא מחלק את אחד המוכפלים" מפעפעת מאיברים של החוג לאידאלים שלו.

נותר לי עוד חור אחד לסגור. נניח ש-{% equation %}\mathfrak{a}{% endequation %} הוא אידאל כלשהו, אז אני רוצה לטעון שקיים אידאל ראשוני {% equation %}\mathfrak{p}{% endequation %} שמחלק אותו, ובניסוח אחר אני רוצה להראות ש-{% equation %}\mathfrak{a}{% endequation %} מוכל באידאל מקסימלי. זו טענה שניתן להוכיח באופן כללי על חוגים - כל אידאל מוכל באידאל מקסימלי; אבל ההוכחה מתבססת על <a href="http://www.gadial.net/?p=37">אקסיומת הבחירה</a> ולכן אנו מעדיפים להחליש את הדרישות עד כמה שניתן, וכאן ניתן להיעזר בכך שהחוג {% equation %}\mathcal{O}{% endequation %} שלנו הוא נתרי. בחוג נתרי מתקיימת תכונה חזקה קצת יותר מאשר "כל אידאל מוכל באידאל מקסימלי" - מתקיימת התכונה שבכל קבוצה לא ריקה של אידאלים קיים איבר מקסימלי. התכונה הזו קריטית בהמשך, לא רק כאן, ולכן כדאי לומר משהו על איך מוכיחים אותה.

ההוכחה טבעית למדי. ניקח אידאל {% equation %}I_{1}{% endequation %} כלשהו בקבוצת האידאלים שנתונה לנו. אם הוא מקסימלי, טוב; אחרת קיים אידאל אחר בקבוצה, {% equation %}I_{2}{% endequation %}, שמכיל אותו. אם הוא מקסימלי, טוב; אחרת, קיים אידאל אחר בקבוצה {% equation %}I_{3}{% endequation %}, שמכיל אותו. ניקח... הבנתם את הרעיון. מתקבלת הסדרה {% equation %}I_{1}\subset I_{2}\subset I_{3}\subset\dots{% endequation %}, אבל מכיוון שהחוג נתרי הסדרה חייבת להיעצר מתישהו - והאיבר שהיא תיעצר בו יהיה איבר מקסימלי (שכן אם לא היה מקסימלי אפשר היה להמשיך את הסדרה גם אחריו). כאן אנחנו משתמשים, באופן כמעט לא מורגש, בגרסה מוחלשת של אקסיומת הבחירה (Axiom of dependent choice); מי שרוצה להיפטר גם מהאקסיומה הזו ייאלץ להגדיר "חוג נתרי" בתור חוג בעל התכונה "לכל קבוצת אידאלים יש איבר מקסימלי", כי היא קריטית לנו.

יפה, עכשיו אפשר לעבור סוף סוף להוכחת משפט הקיום והיחידות של פירוק אידאל לא טריוויאלי {% equation %}\mathfrak{a}\ne\left(0\right),\left(1\right){% endequation %} בחוג דדקינד למכפלה של אידאלים ראשוניים. נתחיל בקיום: נניח בשלילה שקיימים אידאליים לא טריוויאליים שלא קיים להם להם פירוק למכפלת ראשוניים - זוהי קבוצה לא ריקה של אידאלים ולכן קיים בה איבר <strong>מקסימלי</strong> ביחס להכלה, {% equation %}\mathfrak{a}{% endequation %}. לא ייתכן שהוא עצמו ראשוני, שהרי אז הוא כן היה ניתן להצגה כמכפלה של ראשוניים (המכפלה {% equation %}\mathfrak{a}{% endequation %}). מה שאני כן יודע הוא שקיים ראשוני {% equation %}\mathfrak{p}{% endequation %} שמכיל אותו: {% equation %}\mathfrak{a}\subset\mathfrak{p}{% endequation %}. הבה ונכפול את שני האגפים ב-{% equation %}\mathfrak{p}^{-1}{% endequation %}: נקבל {% equation %}\mathfrak{a}\subset\mathfrak{a}\mathfrak{p}^{-1}\subset\mathfrak{p}\mathfrak{p}^{-1}=\mathcal{O}{% endequation %}. אם כן, מצד אחד {% equation %}\mathfrak{a}\mathfrak{p}^{-1}{% endequation %} הוא אידאל לא טריוויאלי (מוכל ממש ב-{% equation %}\mathcal{O}{% endequation %}) ומצד שני הוא מכיל ממש את {% equation %}\mathfrak{a}{% endequation %} ולכן מהמקסימליות ביחס להכלה של {% equation %}\mathfrak{a}{% endequation %} נובע ש-{% equation %}\mathfrak{a}\mathfrak{p}^{-1}{% endequation %} כן ניתן לתיאור כמכפלה של ראשוניים: {% equation %}\mathfrak{a}\mathfrak{p}^{-1}=\mathfrak{p}_{1}\cdots\mathfrak{p}_{t}{% endequation %}. נכפול את שני האגפים ב-{% equation %}\mathfrak{p}{% endequation %}, נקבל את {% equation %}\mathfrak{a}=\mathfrak{p}\mathfrak{p}_{1}\cdots\mathfrak{p}_{t}{% endequation %} וסיימנו. שימו לב עד כמה ההוכחה הזו דומה להוכחה של המשפט עבור {% equation %}\mathbb{Z}{% endequation %}.

גם הוכחת היחידות זה פחות או יותר אותו דבר. נניח ש-{% equation %}\mathfrak{a}=\mathfrak{p}_{1}\cdots\mathfrak{p}_{k}=\mathfrak{q}_{1}\cdots\mathfrak{q}_{t}{% endequation %} כשכל האיברים במכפלות הם ראשוניים, ונתבונן ב-{% equation %}\mathfrak{p}_{1}{% endequation %}: הוא מחלק את {% equation %}\mathfrak{q}_{1}\cdots\mathfrak{q}_{t}{% endequation %} ולכן {% equation %}\mathfrak{p}_{1}|\mathfrak{q}_{i}{% endequation %} עבור {% equation %}i{% endequation %} כלשהו. המשמעות של חלוקה היא, כזכור, ש-{% equation %}\mathfrak{q}_{i}\subseteq\mathfrak{p}_{1}{% endequation %}, אבל {% equation %}\mathfrak{q}_{i}{% endequation %} ראשוני ולכן מקסימלי ולכן אם {% equation %}\mathfrak{p}_{1}\ne\mathcal{O}{% endequation %} מכיל אותו, בהכרח {% equation %}\mathfrak{p}_{1}=\mathfrak{q}_{i}{% endequation %}. כעת נכפול את שני אגפי המשוואה {% equation %}\mathfrak{p}_{1}\cdots\mathfrak{p}_{k}=\mathfrak{q}_{1}\cdots\mathfrak{q}_{t}{% endequation %} ב-{% equation %}\mathfrak{p}_{1}^{-1}{% endequation %} וקיבלנו ש-{% equation %}\mathfrak{p}_{2}\cdots\mathfrak{p}_{k}=\mathfrak{q}_{1}\cdots\mathfrak{q}_{i-1}\mathfrak{q}_{i+1}\cdots\mathfrak{q}_{t}{% endequation %} ואת התהליך הזה ניתן להמשיך באינדוקציה (על מספר האיברים במכפלה, שהוא תמיד מספר טבעי) ולקבל בסופו של דבר שכולם שווים עד כדי שינוי סדר. ממש אותה הוכחה כמו עבור {% equation %}\mathbb{Z}{% endequation %}.

איך זה יצא לנו כל כך פשוט, ממש אותו הדבר? ובכן, ראשית כל בגלל תכונות הנתריות וה"ראשוני גורר אי פריק" שנכונות כאן עבור אידאלים גם אם הן לא נכונות עבור איברים ב-{% equation %}\mathcal{O}{% endequation %} (אפשר לחשוב על חוג דדקינד בתור חוג שבו "האידאלים מתנהגים כמו מספרים נחמדים"), אבל שנית - זה לא פשוט. את החלק היחסית טכני טאטאתי מתחת לשטיח: ההוכחה ש-{% equation %}\mathfrak{a}\mathfrak{p}^{-1}\ne\mathfrak{a}{% endequation %} לכל {% equation %}\mathfrak{a}{% endequation %}. כדי שהפוסט הזה יהיה שלם אני רוצה להוכיח גם את זה, למרות שעכשיו באמת לא יהיה מנוס מנפנופי ידיים כלשהם.

האבחנה הראשונה בדרך להוכחה דווקא לא קשורה בכלל ל-{% equation %}\mathfrak{p}^{-1}{% endequation %}; זוהי האבחנה שלכל אידאל {% equation %}\mathfrak{a}\ne0{% endequation %}, הוא <strong>מחלק</strong> מכפלה של אידאלים ראשוניים: {% equation %}\mathfrak{a}\supseteq\mathfrak{p}_{1}\mathfrak{p}_{2}\dots\mathfrak{p}_{k}{% endequation %}. זה כמובן נובע באופן טריוויאלי מכך שראינו שכל ראשוני ניתן להצגה כמכפלה כזו, אבל אני לא יכול להשתמש בזה - אני עכשיו מוכיח טענת עזר שבה השתמשתי בהוכחה של המשפט על פריקות יחידה! (וההסתרבלות הזו היא כנראה הסיבה שבגללה בספרי מתמטיקה מוכיחים דברים לפי הסדר - קודם הלמות הטכניות והמשעממות ואז האקשן שדורש אותן).

אם כן, מה עושים? משהו לא שונה כל כך ממה שכבר ראינו. אני מניח שקיימים אידאלים שלא מקיימים את התכונה הזו ("לחלק מכפלה של ראשוניים") ובוחר את {% equation %}\mathfrak{a}{% endequation %} להיות המקסימלי שבהם. הוא עצמו לא יכול להיות ראשוני (כי אז היה מכיל מכפלה של ראשוניים - הוא עצמו) ועל פי ההגדרה זה אומר שיש איברים {% equation %}b_{1},b_{2}\in\mathcal{O}{% endequation %} כך ש-{% equation %}b_{1}b_{2}\in\mathfrak{a}{% endequation %} אבל {% equation %}b_{1}\notin\mathfrak{a}{% endequation %} וגם {% equation %}b_{2}\notin\mathfrak{a}{% endequation %}. אז אפשר להרחיב את {% equation %}\mathfrak{a}{% endequation %}: ניקח את {% equation %}\mathfrak{a}_{1}{% endequation %} להיות האידאל הקטן ביותר שמכיל את {% equation %}\mathfrak{a}{% endequation %} ואת {% equation %}b_{1}{% endequation %} (פורמלית: {% equation %}\mathfrak{a}_{1}=\mathfrak{a}+\left(b_{1}\right){% endequation %}) ואת {% equation %}\mathfrak{a}_{2}{% endequation %} להיות הקטן ביותר שמכיל את {% equation %}\mathfrak{a}{% endequation %} ואת {% equation %}b_{2}{% endequation %}. מתקיים ש-{% equation %}\mathfrak{a}\subset\mathfrak{a}_{1}{% endequation %} ו-{% equation %}\mathfrak{a}\subset\mathfrak{a}_{2}{% endequation %} (הכלה ממש בשני המקרים), ומצד שני {% equation %}\mathfrak{a}_{1}\mathfrak{a}_{2}\subseteq\mathfrak{a}{% endequation %} (כי כל איבר של {% equation %}\mathfrak{a}_{1}\mathfrak{a}_{2}{% endequation %} הוא סכום של מכפלות שאו שכוללות איבר מ-{% equation %}\mathfrak{a}{% endequation %} ש"בולע" את השני, או שהן מהצורה {% equation %}b_{1}b_{2}{% endequation %} והנחנו הרי ש-{% equation %}b_{1}b_{2}\in\mathfrak{a}{% endequation %}). כעת, בגלל תכונת המקסימליות של {% equation %}\mathfrak{a}{% endequation %} נובע ש-{% equation %}\mathfrak{a}_{1},\mathfrak{a}_{2}{% endequation %} שניהם כן מכילים מכפלה של אידאלים ראשוניים, ולכן {% equation %}\mathfrak{a}_{1}\mathfrak{a}_{2}{% endequation %} מכיל את מכפלת שתי המכפלות הללו, ולכן היא מוכלת ב-{% equation %}\mathfrak{a}{% endequation %} וסיימנו.

גם את המשפט הזה אפשר לנסח קודם עבור {% equation %}\mathbb{Z}{% endequation %} ולקבל קצת יותר אינטואיציה - נסו לעשות זאת אם לא הבנתם את ההוכחה.

עכשיו בואו נראה שלכל {% equation %}\mathfrak{p}{% endequation %} ראשוני, {% equation %}\mathfrak{p}^{-1}\ne\mathcal{O}{% endequation %}. כלומר, שתמיד אפשר למצוא איבר "שברי" ב-{% equation %}K{% endequation %} שמכפלתו ב-{% equation %}\mathfrak{p}{% endequation %} תיתן רק שלמים. כאן כבר אין חוכמות - ההוכחה תהיה טכנית למדי.

ניקח איזה שהוא{% equation %}a\in\mathfrak{p}{% endequation %} כך ש-{% equation %}a\ne0{% endequation %}. נשים לב לכך ש-{% equation %}\left(a\right){% endequation %} מכיל מכפלה של אידאלים ראשוניים - זה מה שהראינו לפני רגע. ייתכן ש-{% equation %}\left(a\right){% endequation %} מכיל הרבה מכפלות שכאלו - נבחר מכפלה {% equation %}\mathfrak{p}_{1}\cdots\mathfrak{p}_{k}{% endequation %} כזו שעבורה {% equation %}k{% endequation %} מינימלי (כלומר, אין מכפלה של פחות אידאלים שמוכלת ב-{% equation %}\left(a\right){% endequation %}). מכיוון ש-{% equation %}\mathfrak{p}_{1}\cdots\mathfrak{p}_{k}\subseteq\left(a\right)\subseteq\mathfrak{p}{% endequation %} עולה ש-{% equation %}\mathfrak{p}{% endequation %} מחלק את המכפלה ולכן מחלק את אחד מאבריה - בלי הגבלת הכלליות נניח שהוא מחלק את {% equation %}\mathfrak{p}_{1}{% endequation %}, ומכיוון ש-{% equation %}\mathfrak{p}_{1}{% endequation %} ראשוני בהכרח {% equation %}\mathfrak{p}=\mathfrak{p}_{1}{% endequation %} (שימו לב איך אותם טיעונים צצים שוב ושוב).

כעת, לא ייתכן ש-{% equation %}\mathfrak{p}_{2}\cdots\mathfrak{p}_{k}\subseteq\left(a\right){% endequation %} כי במכפלה הזו יש רק {% equation %}k-1{% endequation %} מוכפלים וזה יסתור את המינימליות של {% equation %}k{% endequation %}. לכן יש {% equation %}b\in\mathfrak{p}_{2}\cdots\mathfrak{p}_{k}{% endequation %} כך ש-{% equation %}b\notin a\cdot\mathcal{O}{% endequation %} (זו פשוט דרך אחרת לכתוב ש-{% equation %}b{% endequation %} לא שייך ל-{% equation %}\left(a\right){% endequation %}), וזה אומר ש-{% equation %}a^{-1}b\notin\mathcal{O}{% endequation %} (כאן {% equation %}a^{-1}{% endequation %} הוא ההופכי של {% equation %}a{% endequation %} בשדה השברים {% equation %}K{% endequation %} - קיים כזה כי {% equation %}a\ne0{% endequation %}). מצד שני, {% equation %}b\mathfrak{p}\subseteq\left(a\right){% endequation %} (למה?) ולכן {% equation %}a^{-1}b\mathfrak{p}\subseteq\mathcal{O}{% endequation %}, כלומר {% equation %}a^{-1}b\in\mathfrak{p}^{-1}{% endequation %}. קיבלנו שיש ב-{% equation %}\mathfrak{p}^{-1}{% endequation %} איבר שאיננו ב-{% equation %}\mathcal{O}{% endequation %}, כלומר {% equation %}\mathfrak{p}^{-1}\ne\mathcal{O}{% endequation %}, כפי שרצינו.

עכשיו אפשר סוף סוף להגיע לפאנץ': ניקח {% equation %}\mathfrak{a}\ne0{% endequation %} כלשהו ונראה ש-{% equation %}\mathfrak{a}\ne\mathfrak{a}\mathfrak{p}^{-1}{% endequation %}. לצערי, זה גם השלב שבו נפנופי הידיים הופכים להיות הכרח ויש סיכוי סביר שגם חלק מהשורדים עד פה יאבדו אותי. מה שנעשה הוא להניח שמתקיים דווקא {% equation %}\mathfrak{a}=\mathfrak{a}\mathfrak{p}^{-1}{% endequation %} ולהגיע מכך לסתירה על ידי כך שנוכיח ש-{% equation %}\mathfrak{p}^{-1}=\mathcal{O}{% endequation %}. אז ניקח לנו {% equation %}b\in\mathfrak{p}^{-1}{% endequation %}; מטרתנו להוכיח ש-{% equation %}b\in\mathcal{O}{% endequation %}. כאן נכנסת לתמונה הסגירות-בשלמים של {% equation %}\mathcal{O}{% endequation %}: אם נוכיח ש-{% equation %}b{% endequation %} הוא שורש של פולינום מתוקן שמקדמיו נלקחים מתוך {% equation %}\mathcal{O}{% endequation %}, סיימנו.

כאן אני שולף עוד שימוש של הנתריות של {% equation %}\mathcal{O}{% endequation %}. ראינו כבר שהנתריות אומרת שלכל קבוצת אידאלים יש אידאל מקסימלי; היא גם אומרת שכל אידאל {% equation %}\mathfrak{a}{% endequation %} הוא <strong>נוצר סופית</strong>, במובן זה שקיימת קבוצת איברים {% equation %}\alpha_{1},\dots,\alpha_{n}\in\mathfrak{a}{% endequation %} כך שכל איבר של {% equation %}\mathfrak{a}{% endequation %} ניתן לכתיבה כצירוף לינארי של {% equation %}\alpha_{1},\dots,\alpha_{n}{% endequation %} עם מקדמים מ-{% equation %}\mathcal{O}{% endequation %} (למה זה נכון? כי אם האידאל לא היה נוצר סופית אפשר היה לבנות שרשרת עולה של אידאלים - היינו בונים קבוצה של יוצרים ובכל פעם היינו מוסיפים לה איבר שטרם נפרש על ידה).

עכשיו נכנסת לתמונה אלגברה לינארית, ואני אניח ידע בסיסי בה כי יהיה סיפור להסביר את זה כאן מחדש.

כעת, מה קורה כשכופלים את {% equation %}b{% endequation %} ביוצרים הללו? בשל תכונת הבליעה של אידאלים, {% equation %}b\alpha_{i}\in\mathfrak{a}{% endequation %} לכל {% equation %}i{% endequation %}, ולכן אפשר לכתוב {% equation %}b\alpha_{i}=\sum_{j=1}^{n}a_{ij}\alpha_{j}{% endequation %} עם מקדמים {% equation %}a_{ij}\in\mathcal{O}{% endequation %}. את הדבר הזה אפשר לכתוב בצורה קומפקטית בעזרת מטריצות: נגדיר את המטריצה {% equation %}A{% endequation %} כך ש-{% equation %}A_{ij}=b\delta_{ij}-a_{ij}{% endequation %} כש-{% equation %}\delta_{ij}{% endequation %} היא הדלתא של קרונקר ({% equation %}\delta_{ii}=1{% endequation %} ו-{% equation %}\delta_{ij}=0{% endequation %} אם {% equation %}i\ne j{% endequation %}), אז {% equation %}A\cdot\overline{\alpha}=0{% endequation %} כש-{% equation %}\alpha{% endequation %} הוא וקטור היוצרים {% equation %}\alpha=\left(\alpha_{1},\dots,\alpha_{n}\right){% endequation %}. מכיוון שקיים וקטור שכשכופלים את {% equation %}A{% endequation %} בו מקבלים 0, המטריצה {% equation %}A{% endequation %} היא סינגולרית, כלומר {% equation %}\det A=0{% endequation %}. במילים אחרות, {% equation %}b{% endequation %} הוא שורש של הפולינום המתוקן {% equation %}f\left(x\right)=\det\left(x\delta_{ij}-a_{ij}\right){% endequation %} שמקדמיו הם מ-{% equation %}\mathcal{O}{% endequation %}, ולכן סיימנו.

אם כן, זה גומר את ההוכחה הכללית שבחוג דדקינד יש פריקות יחידה לאידאלים ראשוניים. עכשיו יהיה צורך לחזור ולדבר על חוגי שלמים ולהסביר מדוע הם חוגי דדקינד, ומהו אותו "מספר המחלקה" המסתורי שהזכרתי בתחילת הפוסט.