---
title: "תורת הקבוצות - מכפלות קרטזיות כלליות"
layout: post
categories:
  - תורת הקבוצות
tags:
  - מכפלה קרטזית
---

<a href="https://gadial.net/2019/10/21/intro_to_relations/"> בתחילת סדרת הפוסטים</a> שלי על תורת הקבוצות הגדרתי את המושג של <strong>מכפלה קרטזית</strong>. הרעיון היה זה: אם {% equation %}A,B{% endequation %} הן קבוצות, המכפלה הקרטזית שלהן היא הקבוצה {% equation %}A\times B\triangleq\left\{ \left(a,b\right)\ |\ a\in A,b\in B\right\} |{% endequation %} של כל הזוגות הסדורים שבהם האיבר השמאלי נלקח מ-{% equation %}A{% endequation %} והאיבר הימני נלקח מ-{% equation %}B{% endequation %}. זה היה מושג חשוב ושימש אותנו בכל מה שעשינו משם והלאה, ובפרט <a href="https://gadial.net/2020/01/12/what_are_functions/">השתמשנו בו</a> כדי להגדיר <strong>פונקציות</strong>. עכשיו המעגל הולך להיסגר, כשנשתמש בפונקציות כדי להכליל את מושג המכפלה הקרטזית למספר כלשהו של קבוצות, לאו דווקא שתיים.

אני יכול כבר עכשיו לתת את ההגדרה הכללית, אבל לא נבין ממנה כלום בשלב הזה, ובפרט לא למה היא כל כך מסובכת. אז בואו נתחיל בקטן. מכיוון שכבר הגדרנו מכפלה של שתי קבוצות, בואו נגדיר מכפלה של שלוש קבוצות. ברור לגמרי (אני מקווה!) מה <strong>האינטואיציה</strong> מאחורי הגדרה כזו - אני רוצה אוסף של <strong>שלשות סדורות</strong> כמו שבמכפלה קרטזית של שתי קבוצות היה לי אוסף של <strong>זוגות סדורים</strong>. כלומר, אם {% equation %}A,B,C{% endequation %} קבוצות אני רוצה שיתקיים משהו כמו {% equation %}A\times B\times C=\left\{ \left(a,b,c\right)\ |\ a\in A,b\in B,c\in C\right\} {% endequation %} כאשר הרעיון מאחורי שלשה סדורה היא ששתי שלשות סדורות הן שוות אם ורק אם הן שוות "רכיב-רכיב", כלומר {% equation %}\left(a_{1},b_{1},c_{1}\right)=\left(a_{2},b_{2},c_{2}\right){% endequation %} אם ורק אם {% equation %}a_{1}=a_{2}{% endequation %} וגם {% equation %}b_{1}=b_{2}{% endequation %} וגם {% equation %}c_{1}=c_{2}{% endequation %}.

לכאורה יש לנו דרך פשוטה מאוד לעשות את זה: כבר הגדרנו מכפלה קרטזית של שתי קבוצות, למה לא להפעיל את ההגדרה שוב? תחשבו שניה מה קורה עם חיבור: אנחנו מגדירים חיבור רק עבור זוג מספרים, אבל מכאן קל להכליל לשלושה: {% equation %}a+b+c{% endequation %} זה פשוט {% equation %}\left(a+b\right)+c{% endequation %}, כלומר קודם כל מחברים את {% equation %}a{% endequation %} עם {% equation %}b{% endequation %}, מקבלים "תוצאת ביניים" ומחברים אותה עם {% equation %}c{% endequation %}. גם עבור מכפלה קרטזית זה סוג של עובד, בערך... אבל לא מספיק טוב. כי בואו נראה מה קורה על פי ההגדרה היבשה: מכיוון ש-{% equation %}A\times B\triangleq\left\{ \left(a,b\right)\ |\ a\in A,b\in B\right\} |{% endequation %} אנחנו הולכים לקבל ש-

{% equation %}\left(A\times B\right)\times C=\left\{ \left(\left(a,b\right),c\right)\ |\ a\in A,b\in B,c\in C\right\} |{% endequation %}

כלומר, מבחינה פורמלית, {% equation %}\left(A\times B\right)\times C{% endequation %} הוא לא אוסף של <strong>שלשות סדורות</strong> אלא עדיין אוסף של <strong>זוגות סדורים </strong>כך שהאיבר השמאלי בכל זוג הוא בעצמו זוג סדור. זה... לא נשמע בעייתי במיוחד, למה בעצם לא להגדיר שלשה סדורה בדיוק בצורה הזו? הרי גם "זוג סדור" זה לא איזה מושג קדוש שהגיע אלינו מהחלל החיצון אלא מושג ש"מימשנו" בצורה די מכוערת עם קבוצות. ובכן, יש שתי התנגדויות להגדרה הזו: הראשונה, שאז מכפלה קרטזית לא תהיה אסוציאטיבית: {% equation %}A\times\left(B\times C\right){% endequation %} הוא אוסף של זוגות סדורים שבהם <strong>הרכיב הימני</strong> הוא בעצמו זוג סדור. אבל בינינו, זו התנגדות די קטנונית, נכון? פורמליזם שמורמליזם, אפשר בלי הרבה מאמץ לטפל בבעיה הזו. מה שמביא אותנו להתנגדות השניה: <strong>פשוט לא צריך</strong> לטפל בכל הקטנוניות הזו כי ההגדרה הכללית שאביא עוד מעט מטפלת בכל זה "על הדרך" <strong>ובנוסף לכך</strong> מאפשרת לי להגדיר מכפלה קרטזית של מספר א<strong>ינסופי</strong> של קבוצות.

העניין הזה של "מכפלה של מספר אינסופי של קבוצות" הוא לב הסיפור פה. אני יכול להגדיר מכפלה של שלוש וארבע וחמש קבוצות על ידי הפעלות חוזרות ונשנות של מכפלה של שתי קבוצות; אבל אין לי דרך טובה לתת משמעות ל"אינסוף הפעלות" של מכפלה של שתי קבוצות, כמו שאין לי דרך טובה לתת משמעות לחיבור של אינסוף מספרים רק בעזרת הפעלות חוזרות ונשנות של חיבור שני מספרים (לכל הפחות, אני צריך להכניס לתמונה את מושג <strong>הגבול</strong> אבל זה סיפור אחר ו<a href="https://gadial.net/2008/06/17/infinite_series/">סופר בפעם אחרת</a>).

אבל מה זה בעצם אומר, מכפלה של אינסוף קבוצות? כדי לתת אינטואיציה בואו נתחיל עם סימון כללי למכפלה של מספר <strong>סופי</strong> של קבוצות. נניח שיש לי את הקבוצות {% equation %}A_{1},A_{2},\ldots,A_{n}{% endequation %}. האינטואיציה שלי היא שמכפלה של כולן אמורה להיות אוסף של {% equation %}n{% endequation %}-יות סדורות ("{% equation %}n{% endequation %}-יה" הוא סימון מקובל בעברית! נשבע!). כלומר, שזה אמור להיות משהו כזה:

{% equation %}A_{1}\times A_{2}\times\ldots\times A_{n}=\left\{ \left(a_{1},a_{2},\ldots,a_{n}\right)\ |\ a_{1}\in A_{1},a_{2}\in A_{2},\ldots,a_{n}\in A_{n}\right\} {% endequation %}

מבחינה רעיונית זו הכללה ישירה של המכפלה של שתיים ושלוש קבוצות שהראיתי קודם; אבל מבחינה פורמלית לא הגדרתי עדיין מכפלה כזו בכלל. עכשיו, מה אני אמור לשנות כדי לעבור מהמקרה הסופי אל המקרה האינסופי? בצורה מהנה למדי, אני צריך לכתוב <strong>פחות</strong> כדי לעבור למקרה האינסופי:

{% equation %}A_{1}\times A_{2}\times\ldots=\left\{ \left(a_{1},a_{2},\ldots\right)\ |\ a_{1}\in A_{1},a_{2}\in A_{2},\ldots\right\} {% endequation %}

כל מה שעשיתי פה היה להסיר את האיבר ה"אחרון" בסדרה. אבל איך אני יכול לפרמל את זה עכשיו?

התשובה קלה - פונקציות. בואו נסתכל שניה על ה-{% equation %}n{% endequation %}-יה הסדורה {% equation %}\left(a_{1},a_{2},\ldots,a_{n}\right){% endequation %}. מה זה הדבר הזה, בעצם? אלו הרבה ערכים שונים כשלכל אחד מהם יש <strong>מקום</strong> בתוך ה-{% equation %}n{% endequation %}-יה; המקום הזה מסומן על ידי מספר טבעי בין 1 ל-{% equation %}n{% endequation %} - זה <strong>האינדקס</strong> שמתאר את המקום הזה. {% equation %}a_{3}{% endequation %} הוא האיבר במקום מס' 3, כלומר האיבר ש<strong>מאונדקס</strong> על ידי המספר 3. אפשר לחשוב על התהליך שבו אני אומר לעצמי "הממממ, מאוד מעניין מה יש במקום מספר 3! אולי אבדוק מה נמצא שם?" בתור תהליך של הפעלת פונקציה: הקלט הוא המספר 3 (האינדקס של המקום שאני רוצה לבדוק) והפלט הוא האיבר שנמצא במקום הזה, שמובטח לי ששייך לקבוצה {% equation %}A_{3}{% endequation %}.

אז בואו נפרמל את המושג של {% equation %}n{% endequation %}-יה באמצעות פונקציה: הקלט שפונקציה כזו יכולה לקבל הוא אינדקס, כלומר במקרה של {% equation %}n{% endequation %}-יה זה איבר ששייך לקבוצה {% equation %}\left\{ 1,2,\ldots,n\right\} {% endequation %}. הפלט? הוא משהו ששייך <strong>לאחת</strong> מבין הקבוצות {% equation %}A_{1},A_{2},\ldots,A_{n}{% endequation %}; לכן אם אני בא להגדיר את הטווח של הפונקציה, הוא צריך לכלול את האיחוד של הקבוצות הללו ואין צורך בעוד איברים. מכאן שפורמלית, {% equation %}n{% endequation %}-יה סדורה כזו היא פשוט פונקציה {% equation %}f:\left\{ 1,\ldots,n\right\} \to\bigcup_{i=1}^{n}A_{i}{% endequation %}

עכשיו אפשר לכתוב את ההגדרה של מכפלה קרטזית עבור המקרה הסופי באמצעות שימוש בפונקציות:

{% equation %}A_{1}\times A_{2}\times\ldots\times A_{n}\triangleq\left\{ f:\left\{ 1,\ldots,n\right\} \to\bigcup_{i=1}^{n}A_{i}\ |\ \forall i\in\left\{ 1,\ldots,n\right\} :f\left(i\right)\in A_{i}\right\} {% endequation %}

שימו לב לתנאי שבצד ימין של הסוגריים המסולסלים: הוא אומר שלכל אינדקס {% equation %}i{% endequation %}, האיבר {% equation %}f\left(i\right){% endequation %} אכן שייך לקבוצה {% equation %}A_{i}{% endequation %} (הרי בתיאוריה הוא לא <strong>חייב</strong> להיות שייך אליה, הוא רק צריך להיות שייך לאחת מהקבוצות {% equation %}A_{1},\ldots,A_{n}{% endequation %}).

האם הכתיב הזה מסורבל? בוודאי! אז בואו נעבור למקרה האינסופי, שבו הכתיב נהיה <strong>פשוט יותר</strong>. בשביל לפשט עוד יותר, אני אתחיל את האינדקסים מאפס במקום מ-1 כי אצלי הטבעיים כוללים את 0:

{% equation %}A_{0}\times A_{1}\times\ldots\triangleq\left\{ f:\mathbb{N}\to\bigcup_{i=0}^{\infty}A_{i}\ |\ \forall i\in\mathbb{N}:f\left(i\right)\in A_{i}\right\} {% endequation %}

הכתיב קצת יותר פשוט כי עברתי להשתמש בסימן {% equation %}\mathbb{N}{% endequation %}, אבל העיקרון הוא אותו עיקרון. האם סיימתי, אם כן? ובכן, <strong>ממש לא</strong>. הכתיב אצלי מגביל מדי - למה האינדקסים הם רק מספרים טבעיים? למה לא לאפשר קבוצות אחרות של אינדקסים?

על פניו אפשר לשאול למה בעצם צריך קבוצות אחרות של אינדקסים. למה לא להשתמש בטבעיים תמיד? ובכן, לפעמים הטבעיים פשוט לא מספיקים; <strong>אין מספיק טבעיים</strong>. פורמלית, יש קבוצות אינסופיות <strong>שאי אפשר לאנדקס עם הטבעיים</strong>. זה נושא שאני הולך להגיע אליו בהמשך של הפוסטים בתורת הקבוצות, אבל כמובן ש<a href="https://gadial.net/2007/08/29/cantor_diagonal/">כבר הזכרתי בבלוג</a>.

אז אני הולך לסבך טיפה את הסימונים בהגדרה על מנת להגיע למקרה הכללי ביותר, זה שבו האינדקסים לא צריכים להיות הקבוצה {% equation %}\left\{ 1,\ldots,n\right\} {% endequation %} או הקבוצה {% equation %}\mathbb{N}{% endequation %} אלא הם פשוט קבוצה כללית כלשהי {% equation %}\Lambda{% endequation %}. אני לא מניח כלום על ה-{% equation %}\Lambda{% endequation %} הזו; רק שזו קבוצה של איברים. כמקודם, אני מסמן ב-{% equation %}i{% endequation %} איבר כלשהו בקבוצה הזו. עכשיו ניקח את ההגדרה של מכפלה קרטזית למקרה האינסופי ונדחוף את {% equation %}\Lambda{% endequation %} הזו שם. נקבל:

{% equation %}\prod_{i\in\Lambda}A_{i}\triangleq\left\{ f:\Lambda\to\bigcup_{i\in\Lambda}A_{i}\ |\ \forall i\in\Lambda:f\left(i\right)\in A_{i}\right\} {% endequation %}

ההבדל הכי גדול בין ההגדרה הזו לקודמת הוא בכלל באופן שבו אני מסמן את המכפלה - אני משתמש בסימן {% equation %}\prod{% endequation %} שמיועד לתאר מכפלות עם אינדקס, כמו ש-{% equation %}\sum{% endequation %} משמש לתיאור סכומים עם אינדקס. פרט לכך הסימונים די דומים, ואני מקווה ש<strong>עכשיו</strong> ההגדרה הזו די פשוטה; חשבו מה היה קורה אם הייתי מתחיל איתה את הפוסט - האם גם אז היה ברור מה הולך פה בכלל?

עכשיו, בואו נדבר על מקרה פרטי של מכפלות כאלו - המקרה שבו מכפילים את אותה קבוצה {% equation %}A{% endequation %} בעצמה. מתבקש אינטואיטיבית להשתמש בסימן כמו {% equation %}A^{2}{% endequation %} כדי לתאר את {% equation %}A\times A{% endequation %} או {% equation %}A^{3}{% endequation %} כדי לתאר את {% equation %}A\times A\times A{% endequation %} וכן הלאה, אבל מה לגבי מכפלות אינסופיות? ובכן, תכף נראה שזה נותן לנו אינטואיציה לסימון מועיל באופן כללי.

ראשית, בואו ניקח את ההגדרה של מכפלה קרטזית כללית שכתבתי למעלה ונכתוב אותה מחדש במקרה שבו {% equation %}A_{i}=A{% endequation %} לכל {% equation %}i\in\Lambda{% endequation %}. נעבור מההגדרה הזו:

{% equation %}\prod_{i\in\Lambda}A_{i}\triangleq\left\{ f:\Lambda\to\bigcup_{i\in\Lambda}A_{i}\ |\ \forall i\in\Lambda:f\left(i\right)\in A_{i}\right\} {% endequation %}

אל ההגדרה הזו:

{% equation %}\prod_{i\in\Lambda}A\triangleq\left\{ f:\Lambda\to A\right\} {% endequation %}

תראו כמה שהכל נהיה פשוט פתאום: כבר לא צריך שהפונקציה {% equation %}f{% endequation %} תלך אל איחוד כלשהו ולא צריך לדרוש שהתמונות של {% equation %}f{% endequation %} על איברים ספציפיים יהיו שייכים לקבוצות ספציפיות; המכפלה הקרטזית הפכה להיות פשוט קבוצת <strong>כל הפונקציות</strong> מ-{% equation %}\Lambda{% endequation %} אל {% equation %}A{% endequation %}.

עכשיו, מה זה {% equation %}A^{2}{% endequation %}? אפשר לחשוב על זה בתור המכפלה הקרטזית {% equation %}A_{0}\times A_{1}{% endequation %} כאשר {% equation %}A_{0}=A_{1}=A{% endequation %}. כלומר, בתור {% equation %}\prod_{i\in\left\{ 0,1\right\} }A{% endequation %}, כלומר בתור קבוצת הפונקציות {% equation %}f:\left\{ 0,1\right\} \to A{% endequation %}. עכשיו, <a href="https://gadial.net/2019/10/19/what_is_set_theory/">בואו ניזכר</a> ש<strong>הגדרתי</strong> את 2 בתור הקבוצה {% equation %}\left\{ 0,1\right\} {% endequation %}. אז בעצם כשאני כותב {% equation %}A^{2}{% endequation %} אני כותב {% equation %}A^{\left\{ 0,1\right\} }{% endequation %}. במילים אחרות, {% equation %}A^{\left\{ 0,1\right\} }{% endequation %} היא קבוצת כל הפונקציות מ-{% equation %}\left\{ 0,1\right\} {% endequation %} אל {% equation %}A{% endequation %}.

למה אני מקשקש על זה כל כך הרבה? כי הנה ההגדרה הכללית: הסימון {% equation %}A^{B}{% endequation %} משמש אותנו כדי לתאר את קבוצת <strong>כל הפונקציות</strong> מ-{% equation %}B{% endequation %} אל {% equation %}A{% endequation %}. במילים אחרות, זו המכפלה הקרטזית הכללית של {% equation %}A{% endequation %} בעצמה כשקבוצת האינדקסים שלנו היא {% equation %}B{% endequation %}. אז למשל {% equation %}A^{\mathbb{N}}{% endequation %}, שהיא קבוצת הסדרות עם איברים מ-{% equation %}A{% endequation %}, היא בעצם מכפלה קרטזית אינסופית של {% equation %}A{% endequation %} בעצמה.

סיימתי עם ההגדרות אבל אני לא יכול להתאפק וחייב לתאר עוד שאלה אחת שצצה באופן טבעי כשמדברים על מכפלות קרטזיות כלליות. טוב, אולי לא באופן <strong>כל כך </strong>טבעי, כי היא נראית פשוטה ומגוחכת <strong>מדי</strong> מכדי להצדיק התייחסות. עד שזה נושך אותנו בתחת.

אם אני מסתכל על המכפלה {% equation %}A\times\emptyset{% endequation %} אז בבירור זו תהיה הקבוצה הריקה - אין אפשרות ליצור זוג איברים שהימני מביניהם שייך לקבוצה הריקה כי אין בקבוצה הריקה איברים. באופן דומה, כל מכפלה קרטזית שאחד מהמוכפלים בה הוא הקבוצה הריקה תהיה כולה הקבוצה הריקה - בדיוק אותו סיפור כמו כפל "רגיל" והמספר 0. ובכפל רגיל קורה עוד משהו: אנחנו יודעים שאם נכפול מספרים ששונים מאפס, התוצאה תהיה גם כן שונה מאפס. מה קורה עם מכפלה קרטזית של קבוצות?

ובכן, הנה יש לנו טענה: אם {% equation %}\Lambda{% endequation %} היא קבוצת אינדקסים כלשהי ו-{% equation %}\left\{ A_{i}\right\} _{i\in\Lambda}{% endequation %} משפחה של קבוצות כך ש-{% equation %}A_{i}\ne\emptyset{% endequation %} לכל {% equation %}i\in\Lambda{% endequation %} אז {% equation %}\prod_{i\in\Lambda}A_{i}\ne\emptyset{% endequation %}. טענה פשוטה, לא? הנה הוכחה במקרה של שתי קבוצות: אם {% equation %}A\ne\emptyset{% endequation %} אז קיים {% equation %}a\in A{% endequation %} ואם {% equation %}B\ne\emptyset{% endequation %} אז קיים {% equation %}b\in B{% endequation %} ולכן {% equation %}\left(a,b\right)\in A\times B{% endequation %} ולכן {% equation %}A\times B\ne\emptyset{% endequation %}. פשוט ומובן מאליו, לא?

ובכן, בואו ננסה גם באופן כללי: אם {% equation %}A_{i}\ne\emptyset{% endequation %} לכל {% equation %}i\in\Lambda{% endequation %} אז קיים {% equation %}a_{i}\in A_{i}{% endequation %} לכל {% equation %}i\in\Lambda{% endequation %} ולכן אם נגדיר פונקציה {% equation %}f:\Lambda\to\bigcup A_{i}{% endequation %} על ידי {% equation %}f\left(i\right)=a_{i}{% endequation %} נקבל ש-{% equation %}f\in\prod_{i\in\Lambda}A_{i}{% endequation %} ולכן {% equation %}\prod_{i\in\Lambda}A_{i}\ne\emptyset{% endequation %}. פשוט וקל. לא?

לא.

ממש ממש לא.

הו, כמה שזה לא פשוט וקל.

אבל... אבל... למה, בעצם? מה שגוי ב"הוכחה" שלמעלה? צעד אחד, שמבוצע כל כך מהר שקשה לשים אליו לב: הקפיצה מ"נגדיר פונקציה {% equation %}f{% endequation %} על ידי {% equation %}f\left(i\right)=a_{i}{% endequation %}" אל "נקבל ש-{% equation %}f\in\prod_{i\in\Lambda}A_{i}{% endequation %}". כי צריך לזכור שבתורת הקבוצות, <strong>זה שהגדרנו משהו לא אומר שהוא קיים</strong>.

זוכרים את הפרדוקס של ראסל? כל הצרות שלנו התחילו מכך שנתנו הגדרה פשוטה עד כדי גיחוך למשהו, והנחנו שזה אומר שהמשהו הזה קיים; ואז חיש קל הקיום שלנו הוביל לסתירה. זה אילץ אותנו לזנוח את כל גישת ה"אם אפשר להגדיר משהו אז אוטומטית נובע שהוא קיים" - היא מובילה ליותר מדי מוקשים. אז זה שהגדרתי את {% equation %}f{% endequation %} עדיין לא מבטיח לי שהיא קיימת; צריך להוכיח את זה מתוך האקסיומות של תורת הקבוצות.

עבור המקרה של מכפלה של <strong>מספר סופי</strong> קבוצות קל להוכיח את זה. נניח שאני מכפיל את הקבוצות {% equation %}A_{1},\ldots,A_{n}{% endequation %}. ראשית צריך להוכיח שהמספרים {% equation %}1,\ldots,n{% endequation %} קיימים אבל זה קל; זה נובע מהאקסיומה לפיה הקבוצה הריקה {% equation %}\emptyset{% endequation %} קיימת, ואז מאקסיומות הזיווג (אם {% equation %}a,b{% endequation %} קיימים אז גם {% equation %}\left\{ a,b\right\} {% endequation %} קיימת; ובפרט אם {% equation %}a{% endequation %} קיים גם {% equation %}\left\{ a\right\} {% endequation %} קיימת) והאיחוד, שמאפשרות לנו לבנות מתוך {% equation %}n{% endequation %} את {% equation %}n+1\triangleq n\cup\left\{ n\right\} {% endequation %}.

עכשיו, נתחיל מזה שהקבוצה {% equation %}\emptyset{% endequation %} קיימת. מכיוון ש-{% equation %}A_{1}\ne\emptyset{% endequation %} אז קיים {% equation %}a_{1}\in A_{1}{% endequation %} ולכן הזוג {% equation %}\left(1,a_{1}\right){% endequation %} קיים. למה בעצם הזוג הסדור קיים? בואו ניזכר <a href="https://gadial.net/2019/10/21/intro_to_relations/">בהגדרה שנתתי</a> לזוג סדור: {% equation %}\left(a,b\right)=\left\{ \left\{ a\right\} ,\left\{ a,b\right\} \right\} {% endequation %}. אקסיומת הזיווג עושה פה את העבודה: מתוך {% equation %}a,b{% endequation %} היא בונה לנו את {% equation %}\left\{ a\right\} {% endequation %} ואת {% equation %}\left\{ a,b\right\} {% endequation %} ואז משני אלו היא בונה את הקבוצה של {% equation %}\left(a,b\right){% endequation %}. אז זה קל.

עכשיו, אקסיומת הזיווג נותנת לנו את הקבוצה {% equation %}\left\{ \left(1,a_{1}\right)\right\} {% endequation %}. בעזרת זיווג אפשר לבנות גם את {% equation %}\left\{ \left(2,a_{2}\right)\right\} {% endequation %} ואז בעזרת איחוד לקבל את {% equation %}\left\{ \left(1,a_{1}\right),\left(2,a_{2}\right)\right\} {% endequation %}. אפשר להמשיך ככה לכל הקבוצות ואחרי <strong>מספר סופי של צעדים</strong> נגיע לקבוצה {% equation %}\left\{ \left(1,a_{1}\right),\ldots,\left(n,a_{n}\right)\right\} {% endequation %} שהיא הפונקציה המבוקשת.

אבל עבור אינסוף קבוצות זה לא עובד יותר. הקפיצה לאינסוף היא תמיד צעד טריקי. לכאורה, אקסיומת האיחוד עובדת גם עבור מספר אינסופי של קבוצות - אבל זה רק בהנחה שכבר יש לנו <strong>קבוצה שכוללת את כל הקבוצות הללו</strong>. כאן אין לנו את זה. הבעיה הזו כבר אילצה אותנו להוסיף אקסיומה מיוחדת רק כדי לטעון ש-{% equation %}\mathbb{N}{% endequation %} קיימת; והאקסיומה הזו או מנוסחת בתור "קיימת קבוצה אינסופית" (כלשהי) או בצור שמשתמשת איכשהו במבנה האינדוקטיבי הנחמד של {% equation %}\mathbb{N}{% endequation %}. עבור מכפלה קרטזית כללית של קבוצות נזדקק לאקסיומה ייעודית.

ובכן, מה האקסיומה הזו? הנה ניסוח מדויק של מה שאנחנו צריכים: אם {% equation %}\left\{ A_{i}\right\} _{i\in\Lambda}{% endequation %} היא משפחה של קבוצות כך ש-{% equation %}A_{i}\ne\emptyset{% endequation %} לכל {% equation %}i\in\Lambda{% endequation %} אז קיימת {% equation %}f:\Lambda\to\bigcup_{i\in\Lambda}A_{i}{% endequation %} כך ש-{% equation %}f\left(i\right)\in A_{i}{% endequation %} לכל {% equation %}i\in\Lambda{% endequation %}. לאקסיומה הזו יש שם: <strong>אקסיומת הבחירה</strong>. ומה שראינו בפוסט הזה הוא שהיא שקולה לטענה שמכפלה קרטזית כללית של קבוצות היא לא ריקה אם כל הקבוצות במכפלה לא ריקות.

אני רוצה לחזור על הנקודה הזו כי לדעתי זה משהו מבלבל בצורה יוצאת דופן: מה קורה, בעצם, אם אין לנו את אקסיומת הבחירה? הרי הפונקציה הזו שמראה שהמכפלה הקרטזית לא ריקה פשוט... קיימת, לא? ובכן, זו הנקודה: בלי אקסיומת הבחירה אנחנו לא יכולים <strong>להוכיח</strong> שהפונקציה הזו קיימת, והמשמעות של כך (וזה כבר גולש ללוגיקה) הוא שקיים <strong>עולם שמתאים לאקסיומות של תורת הקבוצות</strong> שבו הפונקציה הזו לא קיימת. אפשר לחשוב על זה בתור מין עולם "קטן ומוגבל" שכזה שבו דברים שאולי טבעי לצפות שיתקיימו לא מתקיימים, והבעיה היא שהאקסיומות של תורת הקבוצות לא חזקות מספיק כדי לצעוק על העולם הזה "תסתלק מפה! אתה לא משהו שאנחנו רוצים להחשיב בתור עולם לגיטימי של תורת הקבוצות!".

למעשה, זו בדיוק הדרך להוכיח שאקסיומת הבחירה הזו היא באמת אקסיומה ולא נובעת מיתר האקסיומות - להראות שקיים עולם של תורת הקבוצות שבו היא לא מתקיימת, ויקום <strong>אחר</strong> של תורת הקבוצות שבו היא כן מתקיימת. אבל זה דיון שנקיים בצורה רצינית יותר בהמשך - בינתיים השגנו את המטרה של לדבר על מכפלות קרטזיות ולראות שמתחבא בהן משהו מגניב. 
