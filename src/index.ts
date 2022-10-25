import * as fs from 'fs';

type Store = any;
type Document = any;
type ID= any;


interface Storage1 {

    save(arg0: Store, arg1: Document) : ID;
    get(arg0: Store, arg1: ID): Document; 

}


type Binary = any
type Stream<T> = any
type DocumentAttrs= any


type Data = Text | Binary 
interface Storage2 {

    save(arg0: Store, arg1: Stream<Data>, arg2: DocumentAttrs) : ID;
    get(arg0: Store, arg1: ID): Stream<Data>; 
    getAttr(arg0: Store, arg1: ID): DocumentAttrs; 
}

type Result<T> = any; 


interface Storage {

    save(arg0: Store, arg1: Stream<Data>, arg2: DocumentAttrs) : Promise<ID>;
    get(arg0: Store, arg1: ID): Promise<Stream<Data>>; 
    getAttr(arg0: Store, arg1: ID): Result<DocumentAttrs>; 

    remove(arg0: ID): Result<void>
}



