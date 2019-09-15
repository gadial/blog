---
id: 3387
title: "משפט קנטור-שרדר-ברנשטיין - ועכשיו בגרסת המלון של הילברט!"
date: 2016-11-30 11:19:03
layout: post
categories: 
  - תורת הקבוצות
tags: 
  - המלון של הילברט
  - משפט קנטור-שרדר-ברנשטיין
---
אני הולך לעשות משהו שעדיין לא עשיתי בבלוג - לכתוב <strong>מחדש</strong> פוסט על נושא ש<a href="http://www.gadial.net/2012/01/21/cantor_schroeder-_bernstein_theorem/">כבר יש לי פוסט עליו בדיוק</a>; במקרה הנוכחי, הוכחת משפט קנטור-שרדר-ברנשטיין. כאילו שזה לא מעליב מספיק, אני אתן פה את אותה ההוכחה כמו בפוסט ההוא. אז למה לכתוב פוסט חדש? כי מאז הפוסט ההוא יצא לי להרצות כמה פעמים בקורסי תורת הקבוצות, ואני חושב שאני יכול להעביר את ההוכחה יותר טוב מאשר העברתי אותה אז, אז למה לא לנסות? בניגוד לפוסט ההוא, כאן אני הולך לספר סיפורים עליזים כדי לתת יותר אינטואיציה לגבי מה שהולך פה - ספציפית, אני אספר וריאציה על סיפור <strong>המלון של הילברט</strong>, <a href="http://www.gadial.net/2010/11/08/hilberts_hotel/">שגם עליו יש לי פוסט</a>. נראה לי שמאוד כדאי להדגיש את הנקודה לפיה משפט קנטור-שרדר-ברנשטיין הוא בסך הכל עוד סיפור בסגנון המלון של הילברט, כי המלון של הילברט נראה פשוט ונחמד יחסית, בעוד שההוכחה של קנטור-שרדר-ברנשטיין נתפסת כמפחידה למדי (לפחות על ידי היא נתפסה ככזו).

אני כן מניח שיש לכם היכרות כלשהי עם תורת הקבוצות, ברמה שתאפשר לכם להבין מה אומר משפט קנטור-שרדר-ברנשטיין: הוא אומר שאם {% equation %}A,B{% endequation %} הן קבוצות כך שקיימות פונקציות חד-חד-ערכיות {% equation %}f:A\to B{% endequation %} וגם {% equation %}g:B\to A{% endequation %} אז קיימת פונקציה חד-חד-ערכית ועל {% equation %}h:A\to B{% endequation %}. בניסוח ציורי, זה אומר שאם {% equation %}\left|A\right|\le\left|B\right|{% endequation %} וגם {% equation %}\left|B\right|\le\left|A\right|{% endequation %} אז {% equation %}\left|A\right|=\left|B\right|{% endequation %}. אבל המשפט עושה קצת יותר מכך - הבנייה של {% equation %}h{% endequation %} היא <strong>קונסטרוקטיבית</strong> לגמרי: אני יכול לתת תיאור מפורש של {% equation %}h{% endequation %} שמתבסס על {% equation %}f,g{% endequation %}; אני לא סתם מוכיח ש"קיימת {% equation %}h{% endequation %} כלשהי שעובדת" (אני קצת מרמה כאן - למילה "קונסטרוקטיבית" במתמטיקה יש גם משמעות יותר מוגבלת, ובמשמעות הזו ההוכחה לא קונסטרוקטיבית; אבל זה דיון אחר שאולי נקיים בעתיד).

מה הקשר למלון של הילברט? המלון של הילברט הוא סיפור דיסטופי על עולם שבו מתרחשות זוועות שלא יאומנו. ואני לא מתכוון לקיום של מלון בן אינסוף חדרים, אלא לכך שכדי לאכסן במלון אורח חדש <strong>בועטים החוצה</strong> אורחים קיימים. בואו ניזכר איך זה הולך: בגרסה המקורית של הסיפור יש חדר במלון לכל מספר טבעי. בהתחלה כל החדרים תפוסים. הגיע אורח חדש ורוצה חדר? אין בעיה! <strong>נבעט החוצה</strong> את האורח מחדר מס' 0 ונאכסן במקומו את האורח החדש. אבל עכשיו מה יעשה האורח שהיה בחדר 0? יעזוב את המלון ויכתוב ביקורת ממורמרת באינטרנט? לא! הוא פשוט יעבור לחדר מס' 1. ומה קורה לאורח בחדר מס' 1? <strong>נבעט החוצה</strong> גם כן! וכן הלאה וכן הלאה; בכל פעם אנחנו בועטים אורח החוצה, ואז דואגים לו לפתרון על חשבון אורח אחר.

הקסם שבסיפור הזה הוא שהבעיה של "יש אורח ללא חדר" נפתרת למרות שבעצם בשום שלב לא פתרנו אותה; מה שאנחנו עושים הוא <strong>לדחוק את הבעיה לאינסוף</strong> ואיכשהו זה גורם לה להיעלם. כמובן, אפשר לטעון שהפתרון שלנו הוא רמאי כי ייקח למלון אינסוף זמן עד שהעניינים יסתדרו, אבל קל לספר את הסיפור באופן שעוקף את זה: מה שקורה הוא שכשמגיע אורח חדש, מייד פוקדים על <strong>כל</strong> האורחים במלון לצאת מהחדר שלהם ולעבור לחדר הבא בתור, ואז תוך עשר דקות כולם עוברים ויש לנו חדר ריק שאפשר לאכסן בו את האורח החדש.

ההוכחה של קנטור-שרדר-ברנשטיין עושה בערך את אותו הדבר. בואו נחשוב על {% equation %}A{% endequation %} בתור קבוצת אנשים ועל {% equation %}B{% endequation %} בתור קבוצת חדרים במלון. המטרה שלנו היא למצוא דרך לשכן את כל האנשים במלון כך שלכולם יש חדר בלי התנגשויות <strong>ואין חדר ריק</strong>. מכיוון שאנחנו לא יודעים כלום על הקבוצות {% equation %}A,B{% endequation %} (אי אפשר להניח שהחדרים ממסופרים על ידי המספרים הטבעיים, למשל; ייתכן מאוד ש-{% equation %}B{% endequation %} היא בכלל קבוצת הממשיים, וכדומה) אנחנו חייבים להתחיל עם <strong>משהו</strong>, ולכן מגיעות לעזרתנו הפונקציות {% equation %}f,g{% endequation %}. על {% equation %}f{% endequation %} אפשר לחשוב בתור "שיטה לשכן את כל האורחים במלון באופן שבו לא יהיו התנגשויות אבל אולי יישארו חדרים ריקים" ואילו על {% equation %}g{% endequation %} אפשר לחשוב בתור "שיטה למלא את כל החדרים במלון באורחים אבל ייתכן שיישארו אורחים שאין להם חדר". הפונקציה {% equation %}f{% endequation %} מקבלת אורח ואומרת לאיזה חדר הוא הולך; הפונקציה {% equation %}g{% endequation %} מקבלת חדר ואומרת איזה אורח לשכן בו.

ועכשיו אפשר לספר את סיפור המלון כך: בהתחלה המלון כולו מלא, על ידי שיטת המילוי שהפונקציה {% equation %}g{% endequation %} מתארת. זה אומר שאפשר לחלק את קבוצת האנשים {% equation %}A{% endequation %} לשתי קבוצות: "ברי המזל" שיש להם חדר, ו"הממורמרים" שאין להם חדר. מבחינה מתמטית, קבוצת ברי המזל היא בדיוק {% equation %}g\left(B\right)\triangleq\left\{ g\left(b\right)\ |\ b\in B\right\} {% endequation %}. את קבוצת "הממורמרים" אני אסמן בתור {% equation %}D_{0}\triangleq A/g\left(B\right){% endequation %}, כשהאפס שנמצא פה אמור לרמוז לכם שעוד יהיו המון ממורמרים נוספים בהמשך. כי ככה זה - אנחנו חיים במציאות דיסטופית שבה בועטים אנשים מחדרי המלון שלהם.

הבעיה שלנו עכשיו היא הבעיה הבסיסית של המלון של הילברט, רק עם קבוצה של אנשים במקום עם אדם אחד. אנחנו רוצים לשכן את כל האורחים מ-{% equation %}D_{0}{% endequation %} במלון שהוא כבר עכשיו מלא. מה נעשה? בשלב ראשון, נחליט לכל אדם ב-{% equation %}D_{0}{% endequation %} לאיזה חדר ללכת, כך שלא יהיו התנגשויות עבור האנשים ב-{% equation %}D_{0}{% endequation %}; ובשלב השני <strong>נבעט החוצה</strong> את כל האורחים שכבר נמצאים בחדרים הללו, ולקבוצת כל הממורמרים החדשים הללו נקרא {% equation %}D_{1}{% endequation %}. אחר כך נפעל באותו האופן בדיוק על {% equation %}D_{1}{% endequation %}: נשכן אותה במלון באותה שיטה שבה שיכנו את {% equation %}D_{0}{% endequation %}, נבעט החוצה את מי שכבר בחדרים הללו, נקרא להם {% equation %}D_{2}{% endequation %}, וכן הלאה וכן הלאה.

השאלה שנשאלת כעת היא איך מחליטים עבור כל אדם ב-{% equation %}D_{0}{% endequation %} לאיזה חדר ללכת. התשובה היא שהפונקציה {% equation %}f{% endequation %} באה כאן לעזרתנו. הפונקציה {% equation %}f{% endequation %} יודעת לשכן <strong>את כל האנשים</strong> בקבוצה {% equation %}A{% endequation %} בלי התנגשויות; ברור שהיא יודעת בפרט לשכן את כל האנשים ב-{% equation %}D_{0}{% endequation %} ללא התנגשויות. אם כן, קבוצת החדרים שאנשי {% equation %}D_{0}{% endequation %} יתפסו היא הקבוצה {% equation %}f\left(D_{0}\right){% endequation %}. כעת נשאלת השאלה - מהי קבוצת האנשים שייבעטו החוצה? כל האנשים הללו שייכים לקבוצת "ברי המזל" שהיו במלון כשהמשחק התחיל - ולכן, בהינתן חדר, כדי לגלות את בר המזל שהתגורר בו אני מפעיל את {% equation %}g{% endequation %} על החדר. מכאן ש-{% equation %}g\left(f\left(D_{0}\right)\right){% endequation %} היא הקבוצה המתאימה - "קבוצת כל האנשים שהתגוררו בחדרים שאנשי {% equation %}D_{0}{% endequation %} תפסו". לכן אני מגדיר {% equation %}D_{1}\triangleq g\left(f\left(D_{0}\right)\right){% endequation %}.

עבור {% equation %}D_{2}{% endequation %} העיקרון דומה. מה שכדאי לשים אליו לב הוא שכל החדרים ב-{% equation %}f\left(D_{1}\right){% endequation %} הם חדרים שבהם גרים "ברי מזל". לא ייתכן שמישהו מ-{% equation %}D_{1}{% endequation %} יקבל הקצאה של חדר ששייך כרגע למישהו מ-{% equation %}D_{0}{% endequation %}, מכיוון שגם אנשי {% equation %}D_{1}{% endequation %} וגם אנשי {% equation %}D_{0}{% endequation %} משוכנים באמצעות הפונקציה {% equation %}f{% endequation %} שמונעת התנגשויות. לכן {% equation %}g\left(f\left(D_{1}\right)\right){% endequation %} נותנת לנו את קבוצת "ברי המזל" שפונו מחדרם על מנת לפנות מקום לאנשי {% equation %}D_{1}{% endequation %}, ונסמן {% equation %}D_{2}\triangleq g\left(f\left(D_{1}\right)\right){% endequation %}.

המשחק נמשך באופן הזה ואני מגדיר {% equation %}D_{n+1}\triangleq g\left(f\left(D_{n}\right)\right){% endequation %}. כך לאט לאט אנחנו נוגסים עוד ועוד מקבוצת "ברי המזל" והופכים אותם לממורמרים. עכשיו אני יכול לדבר על קבוצת הממורמרים המלאה: {% equation %}D=\bigcup_{n=0}^{\infty}D_{n}{% endequation %}. אנחנו יודעים שכל מי ששייך ל-{% equation %}D{% endequation %} שוכן בחדר שלו באמצעות {% equation %}f{% endequation %}, וכל מי שלא שייך ל-{% equation %}D{% endequation %} שוכן בחדר שלו באמצעות {% equation %}g{% endequation %}. צריך להיות טיפה זהירים בעניין הסימונים כאן: אם {% equation %}a\in A{% endequation %} מקיים ש-{% equation %}a\notin D{% endequation %} אז החדר של {% equation %}a{% endequation %} לא נתון באמצעות {% equation %}g\left(a\right){% endequation %} - זה ביטוי חסר משמעות, כי התחום של {% equation %}g{% endequation %} הוא {% equation %}B{% endequation %} ולא {% equation %}A{% endequation %}. אפשר לומר את הדבר הבא: מכיוון ש-{% equation %}g{% endequation %} היא חד-חד-ערכית ועל ומכיוון שהיא כמובן על התמונה שלה, {% equation %}g\left(B\right){% endequation %}, קיימת לה פונקציה הופכית {% equation %}g^{-1}:g\left(B\right)\to B{% endequation %}. כעת, מכיוון ש-{% equation %}D_{0}=A\backslash g\left(B\right){% endequation %}, ברור שאם {% equation %}a\notin D{% endequation %} הרי ש-{% equation %}a\in g\left(B\right){% endequation %} ולכן {% equation %}g^{-1}{% endequation %} מוגדרת עליו. לכן אפשר לתת את ההגדרה הבאה של {% equation %}h{% endequation %}:

{% equation %}h\left(a\right)=\begin{cases}f\left(a\right) &amp; a\in D\\g^{-1}\left(a\right) &amp; a\notin D\end{cases}{% endequation %}

כל שנותר להסביר הוא למה {% equation %}h{% endequation %} היא חד-חד-ערכית ועל.

האינטואיציה לגבי מדוע {% equation %}h{% endequation %} על היא קלה: כל חדר במלון היה תפוס בהתחלה, כשהשתמשנו בשיטה {% equation %}g{% endequation %}. אחר כך, אם פינינו אורח מחדר במלון, זה היה רק כדי להכניס לשם מישהו במקומו, אז ברור שכל החדרים במלון יהיו תפוסים גם בשיטה ש-{% equation %}h{% endequation %} מתאר. פורמלית נוכיח זאת כך: יהא {% equation %}b\in B{% endequation %}. המועמד הטבעי להיות האיש שבחדר {% equation %}b{% endequation %} הוא פשוט מי שהיה בו בהתחלה, שזה {% equation %}a=g\left(b\right){% endequation %}. לכן אנחנו צריכים לבדוק מה עלה בגורלו של {% equation %}a{% endequation %}. ייתכן ש-{% equation %}a{% endequation %} היה בר מזל ואף אחד לא פינה אותו מחדרו בשום שלב, כלומר {% equation %}a\notin D{% endequation %}; במקרה זה, {% equation %}h\left(a\right)=g^{-1}\left(a\right)=b{% endequation %} והנה, מצאנו איבר שנותן את {% equation %}b{% endequation %}. אבל ייתכן גם ש-{% equation %}a{% endequation %} פונה מחדרו, כלומר {% equation %}a\in D{% endequation %}. שימו לב לניואנס כאן: {% equation %}a{% endequation %} <strong>פונה מחדרו</strong>; זה לא שלא היה לו חדר מלכתחילה. פורמלית זה אומר ש-{% equation %}a\notin D_{0}{% endequation %} (וזה ברור, כי {% equation %}a\in g\left(B\right){% endequation %} אבל {% equation %}D_{0}=A\backslash g\left(B\right){% endequation %}) ומכאן שאם {% equation %}a\in D{% endequation %} בהכרח {% equation %}a\in D_{n}{% endequation %} כך ש-{% equation %}n\ge1{% endequation %}. למה הניואנס הזה חשוב? כי אם {% equation %}a{% endequation %} <strong>פונה</strong> מחדרו, זה אומר שהוא פונה כדי שמישהו <strong>אחר</strong> ייכנס. המישהו האחר הזה יהיה מי שתופס את החדר בסופו של דבר. איך נגלה מי זה? נשתמש בהגדרה של {% equation %}D_{n}{% endequation %}: אנחנו יודעים ש-{% equation %}D_{n}=g\left(f\left(D_{n-1}\right)\right){% endequation %} (זה נכון לכל {% equation %}n\ge1{% endequation %}) ולכן אם {% equation %}a\in D_{n}{% endequation %} קיים {% equation %}a^{\prime}\in D_{n-1}{% endequation %} כך ש-{% equation %}a=g\left(f\left(a^{\prime}\right)\right){% endequation %}. נפעיל את {% equation %}g^{-1}{% endequation %} על שני האגפים ונקבל {% equation %}b=g^{-1}\left(a\right)=f\left(a^{\prime}\right)=h\left(a^{\prime}\right){% endequation %} - קיבלנו גם במקרה הזה איבר שנותן את {% equation %}b{% endequation %}. זה מסיים את ההוכחה שהפונקציה היא על.

המשמעות של הוכחה ש-{% equation %}h{% endequation %} חד-חד-ערכית היא שבשיטה הסופית שלנו אין שני אנשים ששוכנו באותו החדר. ניקח שני אנשים {% equation %}a_{1},a_{2}{% endequation %} שכאלו. יש שלוש אפשרויות: או ששניהם "ממורמרים" שלא היה להם חדר בהתחלה או שנבעטו מתישהו מהחדר שלהם; או ששניהם "ברי מזל" שהיה להם חדר מההתחלה והם לא נבעטו ממנו; או שאחד הוא ממורמר והשני בר מזל.

במקרה הראשון, שני הממורמרים שוכנו בחדר שלהם בסופו של דבר בעזרת {% equation %}f{% endequation %} שמבטיחה שלא יהיו התנגשויות. פורמלית, אם {% equation %}a_{1},a_{2}\in D{% endequation %} אז {% equation %}h\left(a_{1}\right)=f\left(a_{1}\right){% endequation %} ו-{% equation %}h\left(a_{2}\right)=f\left(a_{2}\right){% endequation %}, ולכן אם {% equation %}h\left(a_{1}\right)=h\left(a_{2}\right){% endequation %} נובע מכך ש-{% equation %}f\left(a_{1}\right)=f\left(a_{2}\right){% endequation %} ומכיוון ש-{% equation %}f{% endequation %} חד-חד-ערכית נובע מכך ש-{% equation %}a_{1}=a_{2}{% endequation %} מה שמסיים את המקרה הזה.

המקרה השני, של שני ברי מזל, דומה: הרי ההתאמה לחדרים ש-{% equation %}g{% endequation %} מגדירה גם כן לא מאפשרת התנגשויות. אם {% equation %}a_{1},a_{2}\notin D{% endequation %} אז אם {% equation %}h\left(a_{1}\right)=h\left(a_{2}\right){% endequation %} נקבל ש-{% equation %}g^{-1}\left(a_{1}\right)=g^{-1}\left(a_{2}\right){% endequation %} ועל ידי הפעלת {% equation %}g{% endequation %} על שני האגפים נקבל {% equation %}a_{1}=a_{2}{% endequation %}.

במקרה השלישי אפשר להניח בלי הגבלת הכלליות ש-{% equation %}a_{1}\in D{% endequation %} ו-{% equation %}a_{2}\notin D{% endequation %}. מה קורה פה, אינטואיטיבית? {% equation %}a_{2}{% endequation %} הוא "בר מזל", כלומר הוא לא פונה אף פעם מהחדר שלו; לעומתו, {% equation %}a_{1}{% endequation %} הוא "ממורמר", וכדי לשכן אותו היה צריך להעיף מישהו אחר מהחדר שלו. לכן לא ייתכן ש-{% equation %}a_{1}{% endequation %} יחלוק חדר עם מישהו שלא היה צריך להעיף מעולם. פורמלית, אם {% equation %}h\left(a_{1}\right)=h\left(a_{2}\right){% endequation %} אז {% equation %}f\left(a_{1}\right)=g^{-1}\left(a_{2}\right){% endequation %}; נפעיל את {% equation %}g{% endequation %} על שני האגפים ונקבל {% equation %}a_{2}=g\left(f\left(a_{1}\right)\right){% endequation %}, שאומר "{% equation %}a_{2}{% endequation %} נבעט מהחדר שלו כדי לפנות מקום ל-{% equation %}a_{1}{% endequation %}". כי אם {% equation %}a_{1}\in D{% endequation %} זה אומר שקיים {% equation %}n{% endequation %} כך ש-{% equation %}a_{1}\in D_{n}{% endequation %}, ואז על פי הגדרה {% equation %}a_{2}\in g\left(f\left(D_{n}\right)\right)=D_{n+1}{% endequation %}, בסתירה להנחה ש-{% equation %}a_{2}\notin D{% endequation %}, ולכן המקרה הזה לא יכול להתרחש כלל. זה מסיים את ההוכחה.

האם כל סיפורי המעשיות על המלון של הילברט עוזרים להבין את ההוכחה או סתם מסרבלים? אתם תגידו. אני יודע בעיקר שככה ההוכחה יותר <strong>כיפית</strong> לי.